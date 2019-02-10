from src import db

class product(db.Model):
    __table_args__ = (
        db.UniqueConstraint('title'),
    )
    id    = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    inventory_count = db.Column(db.Integer)

def build_product_object(product):
    return {
        'id' : product.id,
        'title' : product.title,
        'price' : product.price,
        'invetoryCount' : product.inventory_count
    }
