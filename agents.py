from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Setup the LLM
llm = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

# Create a Blog Content Researcher Agent
blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get the relevant video content for the topic: {topic} from YouTube channels.",
    description="A Senior Blog content researcher from YouTube Videos",
    name="Senior Blog Content Researcher",
    verbose=True,
    memory=True,
    backstory="Expert in Understanding videos from YouTube and providing suggestions.",
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

# Create the Blog Writer Agent
blog_writer = Agent(
    role="Blog Writer from YouTube Videos",
    goal="Narrate the compelling stories about the topic: {topic} from YouTube channels.",
    description="A Senior Blog content writer from YouTube Videos",
    name="Senior Blog Content Writer",
    verbose=True,
    memory=True,
    backstory="With expertise in simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.",
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)