from fastapi import FastAPI
from src.interfaces import api


app = FastAPI(title="Scraper microservice with crawl4ai")

app.include_router(api.router)
