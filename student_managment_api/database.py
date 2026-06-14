from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# sqlalchemy helps python talk to databases

DATABASE_URL = "sqlite:///students.db" 
#Create/use a SQLite database file named students.db.

engine = create_engine(DATABASE_URL) #Connect Python to that database.

SessionLocal = sessionmaker(bind=engine)
# This creates a custom class called SessionLocal.
# SessionLocal is a factory for Sessions. 
# Every time you want to actually read or write to the database, you will instantiate a new session from this (e.g., db = SessionLocal()).
# bind=engine connects this session factory directly to your database pipeline.

Base = declarative_base()