# initialize_db.py
from src.database.db_connection import engine
from src.database.models import Base

# Create all tables
Base.metadata.create_all(engine)
