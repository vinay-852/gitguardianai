import uuid
import asyncio
import os
import gradio as gr
from dotenv import load_dotenv

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from git import get_git_show  
load_dotenv()

session_service = InMemorySessionService()
APP_NAME = "Social Media Post Generator"
USER_ID = "ahsanayaz"


async def run_agent_on_changes(changes: str) -> str:
    SESSION_ID = str(uuid.uuid4())

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={"changes": changes},
    )

    runner = Runner(
        agent=root_agent,
        session_service=session_service,
        app_name=APP_NAME,
    )

    user_query = types.Content(
        role="user",
        parts=[types.Part(text=changes)],
    )

    response_text = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_query,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response_text = event.content.parts[0].text
    return response_text


def generate_suggestions(input_text: str) -> str:
    if input_text.strip().startswith("http"):
        try:
            changes = get_git_show(input_text.strip())
        except Exception as e:
            return f"Error fetching Git data: {e}"
    else:
        changes = input_text

    return asyncio.run(run_agent_on_changes(changes))


iface = gr.Interface(
    fn=generate_suggestions,
    inputs=gr.Textbox(lines=10, label="Enter GitHub URL or Code"),
    outputs=gr.Textbox(lines=10, label="AI Suggestions"),
    title="Git Code/Change Suggestion Agent",
    description="Enter a GitHub URL or paste code to get suggestions using the root_agent",
)

if __name__ == "__main__":
    iface.launch()
