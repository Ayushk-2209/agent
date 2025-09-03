from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

from dotenv import load_dotenv

agent = Agent(
    name = "finance_agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# agent.print_response("what is the current stock price of uber?")
# agent.print_response("what is the current fundamental of uber")
# agent.print_response("what is the current analyst recommendation of uber?")
agent.print_response("what is the current news of uber stock?")
        
