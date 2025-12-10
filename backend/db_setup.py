from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# This is the base class for our tables
Base = declarative_base()

# SQLite database file (will be auto-created)
engine = create_engine('sqlite:///tweets.db')  # tweets.db will appear in backend/

# Session factory to interact with DB
Session = sessionmaker(bind=engine)

# Define the Tweet table
class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    fetched_at = Column(DateTime, default=datetime.utcnow)

# Create tables automatically if they don't exist
Base.metadata.create_all(engine)