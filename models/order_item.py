from extensions import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Column(db.Float, nullable=False)

    product = db.relationship('Product')  # lightweight join

    serialize_rules = ('-order.order_items',)

    @validates("quantity")
    def validate_quantity(self, key, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Quantity must be a positive integer")
        return value

    @validates("price_at_purchase")
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        return value
