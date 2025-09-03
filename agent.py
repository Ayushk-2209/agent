from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

agent = Agent(
    name="basic_agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGoTools()],
    description="You are a news reporter who reports news in simple language in 3 lines along with date and time of news",
    markdown=True
)

# Generate response
agent.print_response("Tell me the recent news of india along with the web URL of the news")