import os
from pydantic_ai import Agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key from environment variable
# Make sure to set OPENAI_API_KEY in your .env file or environment
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")


agent = Agent(model="gpt-4o-mini")


def run_agent(prompt: str) -> str:
    response = agent.run_sync(prompt)
    return response.output

