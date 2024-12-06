from crewai import Agent
from app.services.crew_ai_service.tools import tool,scrapeTool
from ...config import settings
from crewai import LLM

llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.5,
    api_key=settings.GROQ_API_KEY
)

news_researcher = Agent(
    role="Search Agent",
    goal='Find the relevant URL for given the following topic : {topic}',
    backstory=(
        "As a Search agent you task is to find the relevant URL for the given topic"
        "You are responsible for finding the most relevant information on the web"
        "You also have to store the scraped data in the file"
        "and providing a summary of the key points."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[tool,scrapeTool],
    llm=llm,
    use_system_prompt=False  # Add this line
)

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stroies about {topic}",
    backstory=(
    "also what ever data you have got from scraping read those and make a good news"
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[tool],
    llm=llm,
    use_system_prompt=False  # Add this line
)

print("Agents are ready to use")
