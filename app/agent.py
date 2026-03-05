from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

from app.config import llm
from app.database import engine

# Create SQL Database wrapper
db = SQLDatabase(engine)

# Create SQL Agent (new syntax)
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

def run_agent(question: str):
    response = agent_executor.invoke({"input": question})
    return response["output"]