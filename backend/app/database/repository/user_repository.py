from sqlalchemy.orm import Session

import app.database.db_models as models
import app.database.db_schemas as schemas
from fastapi import Depends, HTTPException, status
from typing import Optional
from datetime import datetime, timedelta
from app.models.user_model import UserBase
from app.models.token_model import TokenData, Token
from jose import JWTError, jwt
from app.core.config import SECRET_KEY, ALGORITHM, PWD_CONTEXT, OAUTH2_SCHEME
from app.database.db_connection import SessionLocal

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    # TODO: Works but creates pydantic.error_wrappers.ValidationError: 1 validation error for UserCreate
    hashed_password = hash_password(user.password) 
    db_transaction_category = models.TransactionCategory(name="main")
    db_user = models.User(email=user.email, username=user.username, hashed_password=hashed_password, main_transaction_category=db_transaction_category)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_password(plain_password, hashed_password):
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def hash_password(plain_password) -> str:
    return PWD_CONTEXT.hash(plain_password)


def authenticate_user(db : Session , username: str, password: str):
    user = get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_token(token: str = Depends(OAUTH2_SCHEME)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return token_data



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



