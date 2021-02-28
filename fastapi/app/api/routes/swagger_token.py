import uvicorn

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user_model import UserBase, UserInDB
from app.models.token_model import Token, TokenData
from app.core.config import ACCESS_TOKEN_EXPIRES_MINUTES
from jose import JWTError, jwt
from app.database.repository.user_repository import (
    authenticate_user,
    create_access_token,
    create_user,
    get_user_by_email,
    get_token,
)
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.db_connection import SessionLocal, engine
from sqlalchemy.orm import Session
from datetime import timedelta


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(models.get_db),
):
    user: models.User = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token: str = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}