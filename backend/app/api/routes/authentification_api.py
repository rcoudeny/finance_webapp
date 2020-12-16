from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user_model import UserBase
from app.models.token_model import Token, TokenData
from app.core.config import ACCESS_TOKEN_EXPIRES_MINUTES
from jose import JWTError, jwt
from app.database.repository.user_repository import (
    get_current_user, 
    authenticate_user, 
    create_access_token, 
    create_user, 
    get_user_by_email
)
import app.database.db_models as models
import app.database.db_schemas as schemas
from app.database.db_connection import SessionLocal, engine
from sqlalchemy.orm import Session
from datetime import timedelta


router = APIRouter()



@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(models.get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(models.get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/users/me")
async def read_users_me(db: Session = Depends(models.get_db), current_user = Depends(get_current_user)):
    return get_current_user()