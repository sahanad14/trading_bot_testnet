from bot.client import BinanceFuturesClient
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price

def execute_order(client: BinanceFuturesClient, symbol, side, order_type, quantity, price=None):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    if order_type == "LIMIT":
        price = validate_price(price)
    
    order_response = client.place_order(symbol, side, order_type, quantity, price)
    if 'error' in order_response:
        print(f"❌ Order failed: {order_response['error']}")
    else:
        print(f"✅ Order placed successfully: {order_response}")
    return order_response