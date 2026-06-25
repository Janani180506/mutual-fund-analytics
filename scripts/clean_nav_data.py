import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/hdfc_top100_nav.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Convert date column if present
for col in df.columns:
    if "date" in col.lower():
        df[col] = pd.to_datetime(df[col])

# Save cleaned file
df.to_csv("data/processed/hdfc_top100_nav_clean.csv", index=False)

print("NAV dataset cleaned successfully!")