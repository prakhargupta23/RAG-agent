from langchain.chat_models import init_chat_model
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_agent
from app.config.database import db
from app.agents.prompts import SYSTEM_PROMPT

model = init_chat_model("openai:gpt-4o-mini")

toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()

agent = create_agent(
    model,
    tools,
    system_prompt=SYSTEM_PROMPT,
)