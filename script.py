import os
from dotenv import load_dotenv
from massive import RESTClient

from massive import RESTClient

# Hardcode it for testing (NOT recommended for production)
client = RESTClient(api_key="VOID")

# Test if this works
ticker = "AAPL"
trade = client.get_last_trade(ticker=ticker)
print(trade)