from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    date = Column(Integer)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    provider_id = Column(Integer, foreign_key=True)
    category_id = Column(Integer, foreign_key=True)
    author_id = Column(Integer, foreign_key=True)

class News_Provider(Base):
    __tablename__ = "news_provider"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)

class News_Category(Base):
    __tablename__ = "news_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(Integer)
    updatet_at = Column(Integer)

class News_Author(Base):
    __tablename__ = "news_author"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(Integer)
    updatet_at = Column(Integer)

class News_Tag(Base):
    __tablename__ = "news_tag"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(Integer)
    updatet_at = Column(Integer)


database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()
    
Base.metadata.create_all(engine)

