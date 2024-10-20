# # from agents import Agents
# from app.services.crew_ai_service.agents import Agents
# # from tasks import Tasks
# from app.services.crew_ai_service.tasks import Tasks

# from crewai import Crew

# #create filter process
# filter_agent = Agents.get_financial_data()
# #create filter task
# filter_task = Tasks.get_financial_data()
# #assembly crew

# crew = Crew(
#     agents=[filter_agent],
#     tasks=[filter_task]
# )
# #kick off crew
# def maincrew():
#     result = crew.kickoff()
#     print(result)