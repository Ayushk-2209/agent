from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    reasoning=True

)

agent.print_response(
    message="how much time does cheetah to travel from new delhi to mumbai?",
    stream=True
)