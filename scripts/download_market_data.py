import yfinance as yf
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Stocks and indices to download
symbols = {
    "NIFTY50": "^NSEI",
    "SENSEX": "^BSESN",
    "HDFCBANK": "HDFCBANK.NS",
    "SBI": "SBIN.NS",
    "ICICIBANK": "ICICIBANK.NS"
}

for name, ticker in symbols.items():
    print(f"Downloading {name}...")

    df = yf.download(
        ticker,
        start="2022-01-01",
        end="2025-06-01",
        auto_adjust=True
    )

    filename = f"data/raw/{name.lower()}.csv"
    df.to_csv(filename)

    print(f"Saved -> {filename}")

print("\nAll datasets downloaded successfully!")