from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-2.0-flash"

CodeQualityAgent = LlmAgent(
    model=MODEL,
    name="CodeQualityAgent",
    instruction=prompt.CODE_QUALITY_AGENT_PROMPT,
)