from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from database import engine, session
from datetime import datetime

# ORM Base
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Plain text password
    accounts = relationship("Account", back_populates="user", cascade="all, delete-orphan")

    @classmethod
    def create_user(cls, name, email, password):
        user = cls(name=name, email=email, password=password)  
        session.add(user)
        session.commit()
        return user

    @classmethod
    def find_by_email(cls, email):
        return session.query(cls).filter_by(email=email).first()

    @classmethod
    def get_all_users(cls):
        return session.query(cls).all()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    balance = Column(Integer, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")

    @classmethod
    def create_account(cls, user_id, balance=0):
        account = cls(user_id=user_id, balance=balance)
        session.add(account)
        session.commit()
        return account

    @classmethod
    def find_by_id(cls, account_id):
        return session.query(cls).filter_by(id=account_id).first()

    @classmethod
    def get_all_accounts(cls):
        return session.query(cls).all()

    @classmethod
    def deposit(cls, account_id, amount):
        account = cls.find_by_id(account_id)
        if account:
            try:
                account.balance += amount
                session.commit()
                Transaction.create_transaction(account_id, amount, 'deposit')
                return account
            except Exception as e:
                session.rollback()
                print(f"Error during deposit: {e}")
        return None

    @classmethod
    def withdraw(cls, account_id, amount):
        account = cls.find_by_id(account_id)
        if account and account.balance >= amount:
            try:
                account.balance -= amount
                session.commit()
                Transaction.create_transaction(account_id, amount, 'withdraw')
                return account
            except Exception as e:
                session.rollback()
                print(f"Error during withdrawal: {e}")
        return None


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String(10), nullable=False)  # 'deposit' or 'withdraw'
    timestamp = Column(DateTime, default=datetime.utcnow)
    account = relationship("Account", back_populates="transactions")

    @classmethod
    def create_transaction(cls, account_id, amount, transaction_type):
        transaction = cls(account_id=account_id, amount=amount, transaction_type=transaction_type)
        session.add(transaction)
        session.commit()
        return transaction

    @classmethod
    def get_by_account_id(cls, account_id):
        return session.query(cls).filter_by(account_id=account_id).all()


# Create tables in the database
Base.metadata.create_all(engine)
