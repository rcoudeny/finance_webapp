from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from .db_connection import Base
from app.database.db_connection import engine, SessionLocal


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    hashed_password = Column(String)

    transaction_categories = relationship("TransactionCategory", back_populates="owner")


class TransactionCategory(Base):
    __tablename__ = "transaction_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    parent_category_id = Column(Integer, ForeignKey("transaction_categories.id"))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="transaction_categories")
    parent_category = relationship(
        "TransactionCategory", back_populates="sub_categories"
    )
    sub_categories = relationship(
        "TransactionCategory",
        remote_side=[parent_category_id],
        cascade="all, delete-orphan",
    )

    transactions = relationship(
        "Transaction", back_populates="category", cascade="all, delete-orphan"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    amount = Column(Float)
    opponent = Column(String)
    opponent_account = Column(String)
    comment = Column(String)
    own_account = Column(String)
    category_id = Column(Integer, ForeignKey("transaction_categories.id"))

    category = relationship("TransactionCategory", back_populates="transactions")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()