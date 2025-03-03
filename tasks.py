from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Identify the topic: {topic}", 
        "Get detailed information about the video from the channel."
        ),
    expected_output="A Comprehensive 3-4 paragraph long report on the {topic} of video content",
    tools=[yt_tool],
    agent=blog_researcher
)

writing_task = Task(
    description=(
        "Get the information from YouTube about the topic: {topic}", 
        ),
    expected_output="Summarize the info from the YouTube channel video on the topic: {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False, # When set to true, agents work asynchronously (parallelly)
    output_file="new-blog-post.md"
)