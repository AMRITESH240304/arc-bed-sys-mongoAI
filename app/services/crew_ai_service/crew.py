from crewai import Crew,Process
from app.services.crew_ai_service.tools import tool
from ...config import settings
from app.services.crew_ai_service.agents import finance_researcher,final_researcher
from app.services.crew_ai_service.task import finance_researcher_task,final_task

crew=Crew(
    agents=[finance_researcher,final_researcher],
    tasks=[finance_researcher_task,final_task],
    process=Process.sequential,
    verbose=True
)

def crewKickOf(input:str):
    result=crew.kickoff(inputs={'topic':input})
    return result