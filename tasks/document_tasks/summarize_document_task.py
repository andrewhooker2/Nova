# Creating the Task
from crewai import Task

from agents.document_agents.summarize_document_agent import summarizer_agent
from tools.document_tools.summarize_document_tool import SummaryTool

summary_task = Task(
    description=(
        "Read the provided document and produce a concise summary that highlights the key points."
    ),
    expected_output='A concise paragraph summarizing the key points of the document.',
    tools=[SummaryTool()],
    agent=summarizer_agent,
)