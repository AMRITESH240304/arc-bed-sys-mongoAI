from ..config import settings
from langchain_google_community import GoogleSearchAPIWrapper

class GoogleSearchService:
    def __init__(self):
        self.apikey = settings.GOOGLE_SEARCH_KEY
        self.search_engine_id = settings.SEARCH_ENGINE_ID
        
    async def langSearch(self,query:str,num_of_search_results:int):
        search_Result = GoogleSearchAPIWrapper(google_api_key=self.apikey,google_cse_id=self.search_engine_id,k=num_of_search_results)
        return search_Result.results(query,num_results=num_of_search_results)