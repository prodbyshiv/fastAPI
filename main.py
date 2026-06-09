from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
#"Take all table definitions that inherit from Base and create them in the database."