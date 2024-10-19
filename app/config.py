from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    HOST: str
    PORT: int
    MONGO_URI:str
    GOOGLE_SEARCH_KEY:str
    SEARCH_ENGINE_ID:str

    class Config:
        env_file = "../.env"  

settings = Settings()
