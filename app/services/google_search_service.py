from ..config import settings
from fastapi import HTTPException
import httpx

class GoogleSearchService:
    def __init__(self):
        self.apikey = settings.GOOGLE_SEARCH_KEY
        self.search_engine_id = settings.SEARCH_ENGINE_ID
        self.baseurl = "https://www.googleapis.com/customsearch/v1"
        
    async def search(self,query:str,num_of_search_results:int):
        url = f"{self.baseurl}?key={self.apikey}&cx={self.search_engine_id}&q={query}&num={num_of_search_results}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
            
            result = response.json()
            items = result.get("items", [])
            
            formatted_results = [
                {"title": item.get("title"), "link": item.get("link")}
                for item in items
            ]
            
            return formatted_results