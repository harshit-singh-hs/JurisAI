from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List
import os
import sys

# Ensure modules can be imported
sys.path.append(os.path.dirname(__file__))

from models.api_models import (
    ChatRequest,
    ChatResponse,
    UserAuth,
    TokenResponse,
    ChatSessionInfo,
    ChatMessageInfo
)
from agents.graph import graph_app
from agents.auth import get_current_user, create_access_token
from database.user_db import (
    create_user,
    get_user_by_email,
    verify_password,
    create_chat,
    get_chat_owner,
    get_user_chats,
    delete_chat,
    get_chat_messages,
    add_message,
    update_chat_title
)

app = FastAPI(title="Online Legal Advisor API")

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Endpoints that touch SQLite, bcrypt or the LLM are plain `def` so FastAPI runs them in a
# threadpool; as `async def` they blocked the event loop and stalled every other request.

def require_chat_owner(session_id: str, user_id: int, action: str):
    """Raise 404/403 unless the chat exists and belongs to user_id."""
    owner_id = get_chat_owner(session_id)
    if owner_id is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    if owner_id != user_id:
        raise HTTPException(status_code=403, detail=f"Not authorized to {action} this chat")

@app.get("/")
async def root():
    return FileResponse(os.path.join(static_dir, "index.html"))

# Auth Endpoints
@app.post("/api/auth/register", response_model=TokenResponse)
def register(auth: UserAuth):
    email = auth.email.strip()
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Please enter a valid email address")
    # bcrypt rejects passwords longer than 72 bytes
    if not 8 <= len(auth.password.encode("utf-8")) <= 72:
        raise HTTPException(status_code=400, detail="Password must be between 8 and 72 characters")

    user = get_user_by_email(email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_id = create_user(email, auth.password)
    if not user_id:
        raise HTTPException(status_code=500, detail="Failed to create user")

    access_token = create_access_token(data={"sub": email})
    return TokenResponse(access_token=access_token, email=email)

@app.post("/api/auth/login", response_model=TokenResponse)
def login(auth: UserAuth):
    user = get_user_by_email(auth.email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(auth.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": auth.email.strip()})
    return TokenResponse(access_token=access_token, email=auth.email.strip())

@app.get("/api/auth/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {"email": current_user["email"]}

# Chat Endpoints
@app.get("/api/chats", response_model=List[ChatSessionInfo])
def get_chats(current_user: dict = Depends(get_current_user)):
    chats = get_user_chats(current_user["id"])
    return [
        ChatSessionInfo(
            id=c["id"],
            title=c["title"],
            created_at=str(c["created_at"])
        ) for c in chats
    ]

@app.get("/api/chats/{session_id}/messages", response_model=List[ChatMessageInfo])
def get_messages(session_id: str, current_user: dict = Depends(get_current_user)):
    owner_id = get_chat_owner(session_id)
    if owner_id is None:
        return []

    if owner_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this chat")

    messages = get_chat_messages(session_id)
    return [ChatMessageInfo(role=m["role"], content=m["content"]) for m in messages]

@app.delete("/api/chats/{session_id}")
def delete_user_chat(session_id: str, current_user: dict = Depends(get_current_user)):
    require_chat_owner(session_id, current_user["id"], "delete")

    delete_chat(session_id, current_user["id"])
    # Also drop the agent's conversation memory for this chat
    try:
        graph_app.checkpointer.delete_thread(session_id)
    except Exception as e:
        print(f"Error deleting checkpoints for {session_id}: {e}")
    return {"status": "success"}


@app.patch("/api/chats/{session_id}/title")
def update_chat_title_endpoint(session_id: str, payload: dict, current_user: dict = Depends(get_current_user)):
    title = payload.get("title") if isinstance(payload, dict) else None
    if not title or not isinstance(title, str):
        raise HTTPException(status_code=400, detail="Title is required")
    title = title.strip()[:100]

    require_chat_owner(session_id, current_user["id"], "update")

    update_chat_title(session_id, title)
    return {"status": "success", "title": title}

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest, current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    session_id = request.session_id

    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # The session id doubles as the agent's memory thread, so never let a user write into
    # (or read the memory of) someone else's chat
    owner_id = get_chat_owner(session_id)
    if owner_id is not None and owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this chat")

    try:
        # Create the chat first so the message rows always reference an existing chat
        if owner_id is None:
            try:
                from agents.llm_setup import get_llm
                from agents.prompts import SESSION_TITLE_PROMPT
                from langchain_core.prompts import PromptTemplate
                llm = get_llm()
                prompt = PromptTemplate.from_template(SESSION_TITLE_PROMPT)
                chain = prompt | llm
                title_response = chain.invoke({"message": request.message})
                title = title_response.content.strip().replace('"', '').replace("'", "").replace('\n', ' ')
                if not title or len(title) > 50:
                    title = request.message[:40] + "..." if len(request.message) > 40 else request.message
            except Exception as e:
                print(f"Error generating title: {e}")
                title = request.message[:40] + "..." if len(request.message) > 40 else request.message
            create_chat(session_id, user_id, title)

        # Save user message to persistent DB
        add_message(session_id, "user", request.message)

        initial_state = {
            "query": request.message,
            "category": "",
            "context": [],
            "draft_response": "",
            "final_response": "",
            "needs_clarification": False
        }

        config = {"configurable": {"thread_id": session_id}}

        # Run the LangGraph workflow
        result = graph_app.invoke(initial_state, config=config)

        # Save assistant response to DB
        add_message(session_id, "ai", result["final_response"])

        return ChatResponse(response=result["final_response"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
