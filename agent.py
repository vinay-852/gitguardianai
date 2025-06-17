from agents.PerformanceAgent import PerformanceAgent
from agents.CodeQualityAgent import CodeQualityAgent
from agents.SecurityAgent import SecurityAgent
from google.adk.agents import ParallelAgent, SequentialAgent, LlmAgent
import prompt

parallel_review_agent = ParallelAgent(
    name="ParallelCodeReviewAgent",
    sub_agents=[CodeQualityAgent, PerformanceAgent, SecurityAgent],
    description="Executes CodeQuality, Performance, and Security agents in parallel on changed Python code."
)

merger_agent = LlmAgent(
    name="CodeReviewMergerAgent",
    description="Merges results from CodeQuality, Performance, and Security agents into a single report.",
    instructions=prompt.ORCHESTRATOR_AGENT_PROMPT,
)

sequential_code_review_agent = SequentialAgent(
    name="CodeReviewOrchestratorAgent",
    sub_agents=[parallel_review_agent, merger_agent],
    description="Coordinates code quality, performance, and security review, then synthesizes the results."
)

root_agent = sequential_code_review_agent