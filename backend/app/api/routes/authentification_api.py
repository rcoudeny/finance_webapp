from app.models.user_model import AuthorizedUser
from pydantic.types import Json
import uvicorn

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.token_model import Token
from app.core.config import ACCESS_TOKEN_EXPIRES_MINUTES
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

# /api/authentification/signin
@router.post("/signin", response_model=AuthorizedUser)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(models.get_db),
) -> AuthorizedUser:
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
    return AuthorizedUser(username=user.username, email=user.email, token=access_token)


@router.post("/signup", response_model=AuthorizedUser)
def register(user: schemas.UserCreate, db: Session = Depends(models.get_db)):
    db_user: models.User = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(db, user)
    access_token_expires: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token: str = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return AuthorizedUser(username=user.username, email=user.email, token=access_token)


@router.get(
    "/currentuser",
    response_description="Get the current user",
    response_model=AuthorizedUser,
)
async def read_users_me(
    token: str = Depends(get_token), db: Session = Depends(models.get_db)
) -> AuthorizedUser:
    user: models.User = get_user_by_email(db, token.email)
    return AuthorizedUser(username=user.username, email=user.email, token=token)
