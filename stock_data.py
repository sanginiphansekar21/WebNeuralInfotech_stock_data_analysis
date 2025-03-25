import yfinance as yf
import pandas as pd

# Define stock symbol and date range
stock_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2024-01-01"

# Fetch stock data
df = yf.download(stock_symbol, start=start_date, end=end_date)

# Save to CSV
df.to_csv("historical_stock_data.csv")

# Print first 5 rows
print(df.head())
