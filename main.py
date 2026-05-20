from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
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

@app.get("/")
async def root():
    return FileResponse(os.path.join(static_dir, "index.html"))

# Auth Endpoints
@app.post("/api/auth/register", response_model=TokenResponse)
async def register(auth: UserAuth):
    user = get_user_by_email(auth.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = create_user(auth.email, auth.password)
    if not user_id:
        raise HTTPException(status_code=500, detail="Failed to create user")
        
    access_token = create_access_token(data={"sub": auth.email.strip()})
    return TokenResponse(access_token=access_token, email=auth.email)

@app.post("/api/auth/login", response_model=TokenResponse)
async def login(auth: UserAuth):
    user = get_user_by_email(auth.email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(auth.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
        
    access_token = create_access_token(data={"sub": auth.email.strip()})
    return TokenResponse(access_token=access_token, email=auth.email)

@app.get("/api/auth/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return {"email": current_user["email"]}

# Chat Endpoints
@app.get("/api/chats", response_model=List[ChatSessionInfo])
async def get_chats(current_user: dict = Depends(get_current_user)):
    chats = get_user_chats(current_user["id"])
    return [
        ChatSessionInfo(
            id=c["id"], 
            title=c["title"], 
            created_at=str(c["created_at"])
        ) for c in chats
    ]

@app.get("/api/chats/{session_id}/messages", response_model=List[ChatMessageInfo])
async def get_messages(session_id: str, current_user: dict = Depends(get_current_user)):
    # Verify owner
    import sqlite3
    from database.user_db import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM chats WHERE id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return []
    
    if row[0] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this chat")
        
    messages = get_chat_messages(session_id)
    return [ChatMessageInfo(role=m["role"], content=m["content"]) for m in messages]

@app.delete("/api/chats/{session_id}")
async def delete_user_chat(session_id: str, current_user: dict = Depends(get_current_user)):
    # Verify owner
    import sqlite3
    from database.user_db import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM chats WHERE id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Chat not found")
    if row[0] != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this chat")
        
    delete_chat(session_id, current_user["id"])
    return {"status": "success"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, current_user: dict = Depends(get_current_user)):
    try:
        user_id = current_user["id"]
        session_id = request.session_id
        
        # Save user message to persistent DB
        add_message(session_id, "user", request.message)
        
        # Check if chat exists. If not, create it.
        import sqlite3
        from database.user_db import DB_PATH
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM chats WHERE id = ?", (session_id,))
        exists = cursor.fetchone()
        conn.close()
        
        if not exists:
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
