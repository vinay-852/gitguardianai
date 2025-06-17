from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

SecurityAgent = LlmAgent(
    model=MODEL,
    name="SecurityAgent",
    instruction=prompt.SECURITY_REVIEW_AGENT_PROMPT,
)
