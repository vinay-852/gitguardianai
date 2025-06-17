from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.0-flash"

PerformanceAgent = LlmAgent(
    model=MODEL,
    name="PerformanceAgent",
    instruction=prompt.PERFORMANCE_OPTIMIZATION_AGENT_PROMPT,
)
