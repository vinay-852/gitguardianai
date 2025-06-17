from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.0-flash"

SecurityAgent = LlmAgent(
    model=MODEL,
    name="SecurityAgent",
    instruction=prompt.SECURITY_REVIEW_AGENT_PROMPT,
)
