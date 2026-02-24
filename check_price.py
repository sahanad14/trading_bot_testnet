from binance.client import Client
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Create Binance client for Testnet
client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

# Get current BTCUSDT price
price = client.futures_symbol_ticker(symbol="BTCUSDT")
print(f"Current BTCUSDT price: {price['price']}")