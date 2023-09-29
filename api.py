from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

def _get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fetch_news/{date}")
def fetch_news(date: str):
    return {"date": date}


@app.get("/fetch_news/")
def fetch_news():
    date = _get_current_date()
    
    return {"date": date}
    
