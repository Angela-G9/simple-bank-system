from models import User, Account, Transaction

def display_menu(authenticated=False):
    print("\n=== BANKING SYSTEM MENU ===")
    if not authenticated:
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
    from models import User, Account, Transaction
from database import session

def display_menu(authenticated=False):
    print("\n=== BANKING SYSTEM MENU ===")
    if not authenticated:
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
    else:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. Create Account")
        print("5. View All Users")
        print("6. View All Accounts")
        print("7. Logout")

def main():
    authenticated = False
    current_user = None  # Store logged-in user

    while True:
        display_menu(authenticated)
        choice = input("Choose an option: ")

        if choice == '1' and not authenticated:  # Create User
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            User.create_user(name, email, password)
            print("User created successfully.")

        elif choice == '2' and not authenticated:  # Login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = User.find_by_email(email)
            if user and user.password == password:  # Compare plain text passwords
                authenticated = True
                current_user = user
                print("Login successful.")
            else:
                print("Invalid email or password.")

        elif authenticated:
            if choice == '1':  # Deposit
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to deposit: "))
                account = Account.deposit(account_id, amount)
                if account:
                    print(f"Deposited {amount}. New balance: {account.balance}")
                else:
                    print("Error: Account not found.")

            elif choice == '2':  # Withdraw
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to withdraw: "))
                account = Account.withdraw(account_id, amount)
                if account:
                    print(f"Withdrawn {amount}. New balance: {account.balance}")
                else:
                    print("Error: Insufficient balance or account not found.")

            elif choice == '3':  # View Transactions
                account_id = int(input("Enter account ID for transaction history: "))
                transactions = Transaction.get_by_account_id(account_id)
                if transactions:
                    for transaction in transactions:
                        print(f"ID: {transaction.id}, Amount: {transaction.amount}, Type: {transaction.transaction_type}, Time: {transaction.timestamp}")
                else:
                    print("No transactions found.")

            elif choice == '4':  # Create Account
                balance_input = input("Enter initial balance (or press Enter for 0): ")
                balance = int(balance_input) if balance_input else 0
                Account.create_account(current_user.id, balance)
                print("Account created successfully.")

            elif choice == '5':  # View All Users
                users = User.get_all_users()
                for user in users:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

            elif choice == '6':  # View All Accounts
                accounts = Account.get_all_accounts()
                for account in accounts:
                    print(f"ID: {account.id}, Balance: {account.balance}, User ID: {account.user_id}")

            elif choice == '7':  # Logout
                authenticated = False
                current_user = None
                print("Logged out successfully.")

        elif choice == '3' and not authenticated:  # Exit
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

else:
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Transaction History")
        print("4. Create Account")
        print("5. View All Users")
        print("6. View All Accounts")
        print("7. Logout")

def main():
    authenticated = False
    current_user = None  

    while True:
        display_menu(authenticated)
        choice = input("Choose an option: ")

        if choice == '1' and not authenticated:  # Create User
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            User.create_user(name, email, password)
            print("User created successfully.")

        elif choice == '2' and not authenticated:  # Login
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = User.find_by_email(email)
            if user and user.verify_password(password):
                authenticated = True
                current_user = user
                print("Login successful.")
            else:
                print("Invalid email or password.")

        elif authenticated:
            if choice == '1':  # Deposit Money
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to deposit: "))
                account = Account.deposit(account_id, amount)
                if account:
                    print(f"Deposited {amount}. New balance: {account.balance}")
                else:
                    print("Deposit failed. Please check your account.")

            elif choice == '2':  # Withdraw Money
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to withdraw: "))
                account = Account.withdraw(account_id, amount)
                if account:
                    print(f"Withdrawn {amount}. New balance: {account.balance}")
                else:
                    print("Insufficient funds or account not found.")

            elif choice == '3':  # View Transactions
                account_id = int(input("Enter account ID for transaction history: "))
                transactions = Transaction.get_by_account_id(account_id)
                if transactions:
                    for transaction in transactions:
                        print(f"ID: {transaction.id}, Amount: {transaction.amount}, Type: {transaction.transaction_type}, Time: {transaction.timestamp}")
                else:
                    print("No transactions found.")

            elif choice == '4':  # Create Account
                balance_input = input("Enter initial balance (or press Enter for 0): ")
                balance = int(balance_input) if balance_input else 0
                account = Account.create_account(current_user.id, balance)
                print(f"Account created successfully with ID {account.id}.")

            elif choice == '5':  # View All Users
                users = User.get_all_users()
                for user in users:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

            elif choice == '6':  # View All Accounts
                accounts = Account.get_all_accounts()
                for account in accounts:
                    print(f"ID: {account.id}, Balance: {account.balance}, User ID: {account.user_id}")

            elif choice == '7':  # Logout
                authenticated = False
                current_user = None
                print("Logged out successfully.")

        elif choice == '3' and not authenticated:  # Exit
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from database import engine, session
from datetime import datetime

# ORM BASE
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

    @classmethod
    def deposit(cls, account_id, amount):
        account = cls.find_by_id(account_id)
        if account:
            account.balance += amount
            session.commit()
            Transaction.create_transaction(account_id, amount, 'deposit')
            return account
        return None

    @classmethod
    def withdraw(cls, account_id, amount):
        account = cls.find_by_id(account_id)
        if account and account.balance >= amount:
            account.balance -= amount
            session.commit()
            Transaction.create_transaction(account_id, amount, 'withdraw')
            return account
        return None

    @classmethod
    def find_by_id(cls, account_id):
        return session.query(cls).filter_by(id=account_id).first()

    @classmethod
    def create_account(cls, balance, user_id):
        account = cls(balance=balance, user_id=user_id)
        session.add(account)
        session.commit()
        return account

    @classmethod
    def get_all_accounts(cls):
        return session.query(cls).all()


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String(10), nullable=False)  # 'deposit' or 'withdraw'
    timestamp = Column(DateTime, default=datetime.utcnow)

    @classmethod
    def create_transaction(cls, account_id, amount, transaction_type):
        transaction = cls(account_id=account_id, amount=amount, transaction_type=transaction_type)
        session.add(transaction)
        session.commit()
        return transaction

    @classmethod
    def get_by_account_id(cls, account_id):
        return session.query(cls).filter_by(account_id=account_id).all()


Base.metadata.create_all(engine)

# CLI Code

def display_menu(authenticated=False):
    print("\n=== BANKING SYSTEM MENU ===")
    if not authenticated:
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
    else:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. Create Account")
        print("5. View All Users")
        print("6. View All Accounts")
        print("7. Logout")

def main():
    authenticated = False
    current_user = None
    
    while True:
        display_menu(authenticated)
        choice = input("Choose an option: ")

        if choice == '1' and not authenticated:
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            User.create_user(name, email, password)
            print("User created successfully.")

        elif choice == '2' and not authenticated:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = User.find_by_email(email)
            if user and user.password == password:
                authenticated = True
                current_user = user
                print("Login successful.")
            else:
                print("Invalid email or password.")

        elif authenticated:
            if choice == '1':
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to deposit: "))
                account = Account.deposit(account_id, amount)
                if account:
                    print(f"Deposited {amount}. New balance: {account.balance}")
                else:
                    print("Account not found.")

            elif choice == '2':
                account_id = int(input("Enter your account ID: "))
                amount = int(input("Enter amount to withdraw: "))
                account = Account.withdraw(account_id, amount)
                if account:
                    print(f"Withdrawn {amount}. New balance: {account.balance}")
                else:
                    print("Insufficient balance or account not found.")

            elif choice == '3':
                account_id = int(input("Enter account ID for transaction history: "))
                transactions = Transaction.get_by_account_id(account_id)
                if transactions:
                    for transaction in transactions:
                        print(f"ID: {transaction.id}, Amount: {transaction.amount}, Type: {transaction.transaction_type}, Time: {transaction.timestamp}")
                else:
                    print("No transactions found.")

            elif choice == '4':
                balance = int(input("Enter initial balance: "))
                Account.create_account(balance, current_user.id)
                print("Account created successfully.")

            elif choice == '5':
                users = User.get_all_users()
                for user in users:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

            elif choice == '6':
                accounts = Account.get_all_accounts()
                for account in accounts:
                    print(f"ID: {account.id}, Balance: {account.balance}, User ID: {account.user_id}")

            elif choice == '7':
                authenticated = False
                current_user = None
                print("Logged out successfully.")

        elif choice == '3' and not authenticated:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
