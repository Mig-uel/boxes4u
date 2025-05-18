from decimal import Decimal


def init_cart():
    return {"items": {}, "subtotal": Decimal(0.00), "total_items": 0}


def get_cart(session):
    return session.get("cart")


def get_cart_items(cart):
    return cart["items"]
