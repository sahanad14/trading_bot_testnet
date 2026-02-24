def validate_symbol(symbol: str):
    if not symbol.isalnum():
        raise ValueError("Symbol must be alphanumeric, e.g., BTCUSDT")
    return symbol.upper()

def validate_side(side: str):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()

def validate_order_type(order_type: str):
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()

def validate_quantity(quantity: str):
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError
        return q
    except:
        raise ValueError("Quantity must be a positive number")

def validate_price(price: str):
    try:
        p = float(price)
        if p <= 0:
            raise ValueError
        return p
    except:
        raise ValueError("Price must be a positive number")