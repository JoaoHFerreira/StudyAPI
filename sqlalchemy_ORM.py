from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
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


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres:///news_fetcher_db')
Session = sessionmaker(bind=engine)
session = Session()

