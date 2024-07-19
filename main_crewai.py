import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

# Initialize the Ollama model
ollama_model = Ollama(model="openhermes")

# Define your agents
researcher = Agent(
    role='Researcher',
    goal='Discover new insights about AI trends',
    backstory="You're a world-class researcher working at a major data science company",
    verbose=True,
    allow_delegation=False,
    llm=ollama_model
)

writer = Agent(
    role='Writer',
    goal='Create engaging content about AI advancements',
    backstory="You're a famous technical writer, specialized in writing data-related content",
    verbose=True,
    allow_delegation=False,
    llm=ollama_model
)

# Create tasks for your agents
task1 = Task(
    description='Investigate the latest AI trends',
    agent=researcher,
    expected_output="A comprehensive report on the latest AI trends"
)

task2 = Task(
    description='Write a blog post on AI advancements',
    agent=writer,
    expected_output="A well-written blog post discussing recent AI advancements"
)

# Instantiate your crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

# Function to run the crew and return the result
def run_crew():
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    result = run_crew()
    print(result)