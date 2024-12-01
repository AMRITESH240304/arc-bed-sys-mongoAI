import os
from ...config import settings

os.environ['SERPER_API_KEY'] = settings.SERPER_API_KEY

from crewai_tools import SerperDevTool
print("Serper is ready to use")

tool = SerperDevTool(n_results=1)