from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///banking_system.db'
engine = create_engine(DATABASE_URL)

# Session
Session = sessionmaker(bind=engine)
session = Session()
