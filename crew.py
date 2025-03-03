from crewai import Crew, Process
from agents import blog_writer, blog_researcher, llm
from tasks import research_task, writing_task

# Create the crew of agents
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential, # Sequential Task is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    chat_llm=llm
)

# Start the crew execution with feedback
result = crew.kickoff(inputs={"topic": "Free Fallin' - Live by John Mayer "})
print(result)