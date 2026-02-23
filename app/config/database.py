# app/config/database.py

import os
import urllib
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")

# Proper Azure SQL connection string
params = urllib.parse.quote_plus(
    f"DRIVER=ODBC Driver 18 for SQL Server;"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
)

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# SQLDatabase wrapper for LangChain
db = SQLDatabase(engine)

def execute_query(query: str, params: dict = None):
    """Executes a SQL query and returns the results as a list of dictionaries."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            if result.returns_rows:
                # Convert rows to dictionaries for easier JSON serialization
                return [dict(row._mapping) for row in result.fetchall()]
            return {"message": "Query executed successfully, no rows returned."}
    except Exception as e:
        print(f"❌ Error running query: {e}")
        raise e

