import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

files = [
    "nifty50.csv",
    "sensex.csv",
    "hdfcbank.csv",
    "sbi.csv",
    "icicibank.csv"
]

for file in files:

    print(f"Cleaning {file}...")

    df = pd.read_csv(f"data/raw/{file}")

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Convert Date column to datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    # Save cleaned file
    output_file = file.replace(".csv", "_clean.csv")
    df.to_csv(f"data/processed/{output_file}", index=False)

    print(f"Saved -> {output_file}")

print("\nMarket datasets cleaned successfully!")