# Binance Futures Testnet Trading Bot

A Python trading bot for **Binance Futures Testnet (USDT-M)**.  
Allows placing **MARKET** and **LIMIT** orders via CLI and checking current prices.  
API keys are safely managed with `.env` files — your real keys are never exposed.

---

## Features

- Place **BUY** or **SELL** orders.
- Supports **MARKET** and **LIMIT** orders.
- CLI-based interface using Typer.
- Logging of orders and errors (locally, not pushed to GitHub).
- Safe API key management using `.env`.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/sahanad14/trading_bot_testnet.git
cd trading_bot_testnet
2. Create a virtual environment (optional but recommended)
conda create -n trading_bot python=3.13
conda activate trading_bot
3. Install dependencies
pip install -r requirements.txt
4. Create .env file
copy .env.example .env  # Windows
# OR
cp .env.example .env    # Mac/Linux

Replace placeholders in .env with your Binance Testnet API key and secret.

Usage
Place an order
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 63200
Check current price
python check_price.py
Examples
1️⃣ Place a MARKET BUY order
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01

Output:

{
  "orderId": 12515131095,
  "symbol": "BTCUSDT",
  "status": "NEW",
  "side": "BUY",
  "type": "MARKET",
  "origQty": "0.010",
  "executedQty": "0.000",
  "avgPrice": "0.00"
}
2️⃣ Place a LIMIT SELL order
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 63200

Output:

{
  "orderId": 12515140208,
  "symbol": "BTCUSDT",
  "status": "NEW",
  "side": "SELL",
  "type": "LIMIT",
  "price": "63200.00",
  "origQty": "0.010",
  "executedQty": "0.000",
  "avgPrice": "0.00"
}
3️⃣ Check current BTCUSDT price
python check_price.py

Output:

Current BTCUSDT price: 63183.50
Logging

Orders and errors are logged in trading_bot.log (local only).

This file is ignored in GitHub to protect sensitive data.

Notes

This bot is connected to Binance Testnet only — it won’t affect your real account.

Never push your .env with real API keys to GitHub. Use .env.example as a safe template.

Author

Sahana D
