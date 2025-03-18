# Simple Banking System

This is a simple banking system implemented in Python using SQLAlchemy for ORM and a CLI for user interaction.

## Features

- Create users and accounts
- Deposit and withdraw money
- View transaction history
- View all users and accounts
- One-to-many relationship between users and accounts

## Requirements

- Python 3.8 or higher
- SQLite database

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Simple-bank-system/simple_banking_system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the database is set up:
   - The database will be automatically created as `banking_system.db` when the application is run.

## Usage

Run the application using:
```bash
python cli.py
```

### Menu Options

1. **Create User**: Register a new user with a name, email, and password.
2. **Login**: Log in with an existing user's email and password.
3. **Deposit Money**: Deposit funds into an account.
4. **Withdraw Money**: Withdraw funds from an account.
5. **View Transaction History**: View all transactions for a specific account.
6. **Create Account**: Create a new account for the logged-in user.
7. **View All Users**: Display all registered users.
8. **View All Accounts**: Display all accounts in the system.
9. **Logout**: Log out of the current session.
10. **Exit**: Exit the application.

## Project Structure

```
simple_banking_system/
├── cli.py          # Command-line interface for user interaction
├── database.py     # Database connection and session setup
├── models.py       # SQLAlchemy models for User, Account, and Transaction
├── requirements.txt # Project dependencies
├── README.md       # Project documentation
└── __pycache__/    # Compiled Python files
```

## Notes

- Passwords are stored in plain text. For production, consider using a hashing library like `bcrypt` for secure password storage.
- Error handling is basic and should be improved for robustness in a production environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.