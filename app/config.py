from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    HOST: str
    PORT: int
    MONGO_URI:str

    class Config:
        env_file = "../.env"  

settings = Settings()
