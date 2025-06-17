from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

PerformanceAgent = LlmAgent(
    model=MODEL,
    name="PerformanceAgent",
    instruction=prompt.PERFORMANCE_OPTIMIZATION_AGENT_PROMPT,
)
