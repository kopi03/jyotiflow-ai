from fastapi import APIRouter, Depends, HTTPException, status, Request
from db import get_db
import jwt
import os
from datetime import datetime, timezone
import uuid
from typing import Dict, Any

router = APIRouter(prefix="/api/user", tags=["User"])

JWT_SECRET = os.getenv("JWT_SECRET", "jyotiflow_secret")
JWT_ALGORITHM = "HS256"

def get_user_id_from_token(request: Request) -> str:
    """Extract user ID from JWT token"""
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = auth.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["user_id"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

# தமிழ் - பயனர் சுயவிவரம் பெறுதல்
@router.get("/profile")
async def get_profile(request: Request, db=Depends(get_db)):
    user_id = get_user_id_from_token(request)
    user = await db.fetchrow("SELECT id, email, full_name, created_at FROM users WHERE id=$1", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": str(user["id"]), "email": user["email"], "full_name": user["full_name"], "created_at": user["created_at"]}

@router.get("/credits")
async def get_credits(request: Request, db=Depends(get_db)):
    user_id = get_user_id_from_token(request)
    user = await db.fetchrow("SELECT credits FROM users WHERE id=$1", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "data": {"credits": user["credits"]}} 