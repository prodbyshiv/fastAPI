from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# sqlalchemy helps python talk to databases

DATABASE_URL = "sqlite:///students.db" 
#Create/use a SQLite database file named students.db.

engine = create_engine(DATABASE_URL) #Connect Python to that database.

SessionLocal = sessionmaker(bind=engine)