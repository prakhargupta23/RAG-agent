from app.agents.sql_agent import get_sql_query
#from app.config.database import execute_query

def ask_question(question: str):
    return get_sql_query(question)

# def fetch_task_data(limit: int = 100):
#     """
#     Business logic to fetch task data from the database.
#     For now, it specifically targets the TaskData table.
#     """
#     query = f"SELECT TOP {limit} * FROM TaskData"
#     return execute_query(query)

# def run_custom_task_query(sql_query: str):
#     """
#     Executes a custom SQL query provided by the user.
#     Restricted to TaskData table for now.
#     """
#     if "TaskData" not in sql_query:
#         # Simple check for security/scope
#         raise ValueError("For now, queries are restricted to the 'TaskData' table.")
    
#     return execute_query(sql_query)

