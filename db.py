from sqlalchemy import create_engine
import pandas as pd
import urllib

# SOURCE CONNECTION
source_conn_str = """
DRIVER={ODBC Driver 18 for SQL Server};
SERVER=nwr.database.windows.net;
DATABASE=pension-production;
UID=sql-admin;
PWD=AcdG8527*;
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

# TARGET CONNECTION
target_conn_str = """
DRIVER={ODBC Driver 18 for SQL Server};
SERVER=nwr.database.windows.net;
DATABASE=pension-prod-2025-9-29-17-7 (1);
UID=sql-admin;
PWD=AcdG8527*;
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

# Convert to SQLAlchemy format
source_engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(source_conn_str)
)

target_engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(target_conn_str)
)

# Read from source table
query = "SELECT * FROM dbo.sbi_master"

df = pd.read_sql(query, source_engine)

# Insert into target
df.to_sql(
    "sbi_master",
    target_engine,
    schema="dbo",
    if_exists="append",
    index=False
)

print(f"{len(df)} rows migrated successfully.")