# app/config/database.py

import os
import urllib
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

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

print("✅ Connected successfully!")

# Fetch 1000 rows
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT SUM(CAST(actualForMonth AS FLOAT)) AS total_working_expenditure FROM WorkingExpenses WHERE category = 'TOTAL' AND selectedMonthYear = '12/2025'"))
        rows = result.fetchall()

        print(f"\nFetched {len(rows)} rows\n")

        # Print only first 5 rows to avoid console flood
        for row in rows[:5]:
            print(row)

except Exception as e:
    print("❌ Error running query:", e)