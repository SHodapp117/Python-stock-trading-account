import requests
import os 
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()





# Use it in your URL
URL = f"https://api.massive.com/v3/reference/dividends?apiKey={'MASSIVE_API_KEY'}"

# Make your request
response = requests.get(URL)
print(response.json())