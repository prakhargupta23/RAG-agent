from sqlalchemy import create_engine
import pandas as pd
import urllib

print("🚀 Starting database migration...")

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

print("🔌 Creating database connections...")

source_engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(source_conn_str)
)

target_engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(target_conn_str),
    fast_executemany=True
)

print("✅ Connections established")

# Fetch data
query = "SELECT * FROM dbo.debit"
print("📥 Fetching data from source table...")

df = pd.read_sql(query, source_engine)

print(f"📊 {len(df)} rows fetched from source database")

# Remove unwanted columns
print("🧹 Removing unnecessary columns (createdAt, updatedAt)...")
df = df.drop(columns=["createdAt", "updatedAt"], errors="ignore")

# Convert month column
print("🗓 Converting month column to datetime format...")
df["month"] = pd.to_datetime(df["month"], format="%m/%Y", errors="coerce")

# Filter data between Jan 2024 and Apr 2025
print("🔎 Filtering data between Jan 2024 and Apr 2025...")
start_date = "2024-01-01"
end_date = "2025-04-30"

df = df[(df["month"] >= start_date) & (df["month"] <= end_date)]

print(f"📊 {len(df)} rows remaining after filtering")

# Convert back to MM/YYYY format (if target DB expects that)
df["month"] = df["month"].dt.strftime("%m/%Y")

print(f"📋 Columns being inserted: {list(df.columns)}")

# Insert into target
print("📤 Inserting data into target database...")

df.to_sql(
    "debit",
    target_engine,
    schema="dbo",
    if_exists="append",
    index=False,
    chunksize=500
)

print(f"🎉 Migration complete! {len(df)} rows inserted successfully.")