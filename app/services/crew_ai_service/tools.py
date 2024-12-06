import os
from ...config import settings

os.environ['SERPER_API_KEY'] = settings.SERPER_API_KEY

from crewai_tools import SerperDevTool,ScrapeWebsiteTool
print("Serper is ready to use")

tool = SerperDevTool(n_results=1)
scrapeTool = ScrapeWebsiteTool()

mongoEbeddingTool = 213

"""

1) fix the agents accoridng to use
2) time to impelement the tool for scaraping and embedding  
3) implement a rag for the same

lets do it
  
"""