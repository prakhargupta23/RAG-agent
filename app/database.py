from sqlalchemy import create_engine

MSSQL_URL = (
    "mssql+pyodbc://username:password@server/database?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(MSSQL_URL)