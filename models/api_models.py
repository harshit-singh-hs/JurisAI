from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    session_id: str

class ChatResponse(BaseModel):
    response: str

class UserAuth(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    email: str

class ChatSessionInfo(BaseModel):
    id: str
    title: str
    created_at: str

class ChatMessageInfo(BaseModel):
    role: str
    content: str

