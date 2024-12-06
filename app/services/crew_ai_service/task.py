from crewai import Task
from app.services.crew_ai_service.tools import tool,scrapeTool
from ...config import settings
from app.services.crew_ai_service.agents import news_researcher, news_writer

savingTask = Task(
  description=(
    "Save the latest scrape data"
  ),
  expected_output='A text file containing the latest news data.',
  agent=news_researcher,
  output_file='latest-news.txt'
)

research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  agent=news_researcher,
  output_file='ai-trends-report.txt'
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)