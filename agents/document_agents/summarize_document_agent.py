from crewai import Agent
from tools.document_tools.summarize_document_tool import SummaryTool

# Creating the Agent
summarizer_agent = Agent(
    role='Summarizer',
    goal='Summarize the provided document into a concise paragraph.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert at extracting essential information from texts, making"
        " complex information easily accessible and comprehensible."
    ),
    tools=[SummaryTool()],  # Replace SummaryTool() with the actual tool if different
    allow_delegation=False
)
