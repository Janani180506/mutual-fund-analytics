import sqlite3
import pandas as pd
import os

# Database path
db_path = "bluestock_mf.db"

# Connect to SQLite
conn = sqlite3.connect(db_path)

processed_folder = "data/processed"

for file in os.listdir(processed_folder):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")

        df = pd.read_csv(os.path.join(processed_folder, file))

        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"Loaded {file} -> {table_name}")

conn.close()

print("\nDatabase created successfully!")