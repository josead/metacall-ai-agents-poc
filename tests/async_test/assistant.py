import os
from pydantic_ai import Agent
from dotenv import load_dotenv

## TODO: Add issue in metacall python loader to support `logging` instead of `print`
import logging
import time


def yellow_prefix(text: str) -> str:
    # ANSI escape code for yellow is \033[93m, reset is \033[0m
    return f"\033[93mFrom python:\033[0m {text}"



# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key from environment variable
# Make sure to set OPENAI_API_KEY in your .env file or environment
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")


agent = Agent(model="gpt-4o-mini")


def run_agent(prompt: str) -> str:
    start = time.time()
    print(yellow_prefix(f"[START] {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))} - Running agent with prompt: {prompt}"))
    response = agent.run_sync(prompt)
    end = time.time()
    print(yellow_prefix(f"[END] {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))} - Response: {prompt} {response.output} (duration: {(end - start) * 1000:.2f} ms)"))
    return response.output

async def arun_agent(prompt: str) -> str:
    start = time.time()
    print(yellow_prefix(f"[START] {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))} - Running agent with prompt: {prompt}"))
    response = await agent.run(prompt)
    end = time.time()
    print(yellow_prefix(f"[END] {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))} - Response: {prompt} {response.output} (duration: {(end - start) * 1000:.2f} ms)"))
    return response.output

print(yellow_prefix(f"Hello From Python!"))
