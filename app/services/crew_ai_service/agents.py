from crewai import Agent
from app.services.crew_ai_service.tools import tool
from ...config import settings
from crewai import LLM

llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.5,
    api_key=settings.GROQ_API_KEY
)

news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[tool],
    llm=llm,
    use_system_prompt=False  # Add this line
)

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stroies about {topic}",
    backstory=(
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
