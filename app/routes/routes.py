from fastapi import APIRouter
from ..services.google_search_service import GoogleSearchService
# from ..services.crew_ai_service.crew import maincrew

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from another route!"}

@router.get("/search")
async def search_from_google(query: str,num_of_search_results:int):
    return await GoogleSearchService().langSearch(query, num_of_search_results)

@router.get("/crewkickoff")
async def webcrawl(url:str):
    # await maincrew()
    pass