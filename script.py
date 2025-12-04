import os
from dotenv import load_dotenv
from massive import RESTClient

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("MASSIVE_API_KEY")
client = RESTClient(api_key=api_key)

# Test with endpoints that work on free/basic plans
ticker = "AAPL"

# Try getting ticker details 
try:
    ticker_details = client.get_ticker_details(ticker)
    print("Ticker Details:", ticker_details)
except Exception as e:
    print(f"Ticker details error: {e}")

# Try getting previous close 
try:
    prev_close = client.get_previous_close(ticker)
    print("\nPrevious Close:", prev_close)
except Exception as e:
    print(f"Previous close error: {e}")

# Try getting aggregates/bars 
try:
    aggs = client.get_aggs(ticker, 1, "day", "2024-01-01", "2024-01-31")
    print("\nAggregate Data:", aggs)
except Exception as e:
    print(f"Aggregates error: {e}")