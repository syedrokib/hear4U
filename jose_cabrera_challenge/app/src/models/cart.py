from src import db
from .product import product

class cart(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

def build_cart_object(cart):
    cart_object_products = []
    cart_id = None
    total_price = 0
    for data in cart:
        cart_id = data.id
        cart_object_products.append(
            {
                'productId' : data.product_id,
                'quantity' : data.quantity
            }
        )
        for price in db.session.query(product.price).filter(product.id == data.product_id).one():
            total_price += price * data.quantity

    return {
        'id' : cart_id,
        'products' : cart_object_products,
        'totalPrice' : total_price
    }