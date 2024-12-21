from fastapi import APIRouter
from ..services.google_search_service import GoogleSearchService
from ..services.crew_ai_service.crew import crewKickOf
from ..db.database import storeEmbeddings
from ..services.gemini_service import get_json
from pydantic import BaseModel

router = APIRouter()

class InputModel(BaseModel):
    input: str

def get_json_cleaned(raw_data):
    # Clean up the raw JSON-like string
    cleaned_data = raw_data.replace("\\n", "").replace("'", '"')
    return cleaned_data

@router.get("/hello")
def say_hello():
    return {"message": "Hello from another route!"}

@router.get("/search")
async def search_from_google(query: str,num_of_search_results:int):
    return await GoogleSearchService().langSearch(query, num_of_search_results)

@router.post("/crewkickoff")
async def webcrawl(payload: InputModel):
    storeResult = crewKickOf(payload.input)
    end_result = get_json_cleaned(get_json(storeResult.raw))
    return {"end_result": end_result, "raw_result": storeResult.raw}

@router.get('/testdb')
async def testDB():
    storeEmbeddings()
    return {"message":"DB is working fine"}
