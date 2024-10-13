from fastapi import FastAPI
from .routes import router
from .config import settings
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import connect_to_mongo
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_mongo()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {
        "Hello": "Welcome to the MongoDB AI Hackathon",
        "DB":"MongoDB"
        }

@app.head("/")
def read_head():
    return {}

if __name__ == "__main__":
    port = settings.PORT or int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
