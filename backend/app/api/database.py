from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost/OpenAGI-SimBot"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL.replace("asyncpg", "psycopg2"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()