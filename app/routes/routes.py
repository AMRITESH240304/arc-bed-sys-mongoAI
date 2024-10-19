from fastapi import APIRouter,HTTPException
from ..services.google_search_service import GoogleSearchService
import httpx

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from another route!"}

@router.get("/search")
async def search_from_google(query: str,num_of_search_results:int):
    return await GoogleSearchService().search(query,num_of_search_results)