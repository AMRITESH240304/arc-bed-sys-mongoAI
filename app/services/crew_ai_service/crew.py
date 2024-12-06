from crewai import Crew,Process
from app.services.crew_ai_service.tools import tool
from ...config import settings
from app.services.crew_ai_service.agents import news_researcher, news_writer
from app.services.crew_ai_service.task import research_task, write_task,savingTask

crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[savingTask,research_task,write_task],
    process=Process.sequential,
)

def crewKickOf(input:str):
    result=crew.kickoff(inputs={'topic':input})
    return result