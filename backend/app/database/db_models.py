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
    main_transaction_category_id = Column(Integer, ForeignKey("transaction_categories.id"))

    main_transaction_category = relationship("TransactionCategory", back_populates="owner")
    # transactions = relationship("Transaction", back_populates="owner")

# class Transaction(Base):
#     __tablename__ = "transactions"

#     id = Column(Integer, primary_key=True, index=True)
#     date = Column(Date)
#     amount = Column(Float)
#     opponent = Column(String)
#     opponent_account = Column(String)
#     comment = Column(String)
#     own_account = Column(String)

    # transaction_category_id = Column(Integer, ForeignKey("transaction_categories.id"))
    # owner = relationship("User", back_populates="transactions")

    # category = relationship("TransactionCategory", back_populates="transactions")


class TransactionCategory(Base):
    __tablename__ = "transaction_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    owner = relationship("User", back_populates="main_transaction_category")
    

#     subcategories = relationship("TransactionCategory", back_populates="maincategorie")
#     maincategorie = relationship("TransactionCategory", back_populates="subcategories")
#     transactions = relationship("Transaction", back_populates="category")
    
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()