# app/config/database.py

import os
import urllib
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import pyodbc

print("this is load_dotenv")
load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")

# print("this is username",username)
# print("this is password",password)
# print("this is server",server)
# print("this is database",database)
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
print("this is drivers",pyodbc.drivers())
def fetch_data(query):

    print("✅ Connected successfully!")

    # Fetch 1000 rows
    try:
        with engine.connect() as conn:
            print("this is query",query)
            result = conn.execute(text(query))
            rows = result.fetchall()

            print(f"\nFetched {len(rows)} rows\n")

            # Print only first 5 rows to avoid console flood
            for row in rows[:5]:
                print("hello",row)
            print("this is rows",rows,type(rows))
            return rows

    except Exception as e:
        print("❌ Error running query:", e)
        return None

    