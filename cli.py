import typer
from binance.client import Client
from dotenv import load_dotenv
import os

app = typer.Typer()

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Binance Testnet client
client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

@app.command()
def place(
    symbol: str = typer.Option(..., help="Trading pair, e.g., BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT)")
):
    """
    Place an order on Binance Futures Testnet
    """
    try:
        side = side.upper()
        order_type = order_type.upper()

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type == "LIMIT":
            if price is None:
                typer.echo("❌ Price is required for LIMIT orders.")
                raise typer.Exit()
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
        else:
            typer.echo("❌ Invalid order type. Use MARKET or LIMIT.")
            raise typer.Exit()

        typer.echo(f"✅ Order placed successfully: {order}")
    except Exception as e:
        typer.echo(f"❌ Order failed: {e}")

if __name__ == "__main__":
    app()