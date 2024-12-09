from crewai import Task
from app.services.crew_ai_service.tools import tool, scrapeTool
from ...config import settings
from app.services.crew_ai_service.agents import finance_researcher, final_researcher
from pydantic import BaseModel

class FinancialData(BaseModel):
    company_name: str
    revenue: float
    net_income: float
    total_assets: float
    chart: list

# Define the finance_researcher_task
finance_researcher_task = Task(
    description=(
        "Conduct financial research on the given topic: {topic} "
    ),
    agent=finance_researcher,
    expected_output="Clean and formatted financial data",
    tools=[tool, scrapeTool],
    output_pydantic=FinancialData,
)

# Define the final_task with a proper expected_output
final_task = Task(
    description="Finalize the financial data.",
    agent=final_researcher,
    expected_output="provide me paragraph with all the necessary data",
)
