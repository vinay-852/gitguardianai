import uuid
import asyncio
from dotenv import load_dotenv
import os
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from git import get_git_show

load_dotenv()


async def main():
    changes = get_git_show("https://github.com/vinay-852/gitguardianai.git")
    session_service = InMemorySessionService()

    SESSION_ID = str(uuid.uuid4())
    USER_ID = "ahsanayaz"
    APP_NAME = "Social Media Post Generator"

    # Await session creation, inject 'changes' into state
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state={"changes": changes},
    )

    print(f"Session ID: {session.id}")

    runner = Runner(
        agent=root_agent,
        session_service=session_service,
        app_name=APP_NAME,
    )

    user_query = types.Content(
        role="user",
        parts=[types.Part(text=changes)],
    )

    # Run the agent and print the final response
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_query,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("Final response:", event.content.parts[0].text)

    # Await session retrieval
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

if __name__ == "__main__":
    asyncio.run(main())
