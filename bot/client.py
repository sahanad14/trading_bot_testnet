from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }
            if order_type.upper() == "LIMIT":
                if price is None:
                    raise ValueError("Price must be provided for LIMIT orders")
                params['price'] = price
                params['timeInForce'] = 'GTC'

            logger.info(f"Placing order: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order response: {order}")
            return order
        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"API/Order error: {e}")
            return {'error': str(e)}
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {'error': str(e)}