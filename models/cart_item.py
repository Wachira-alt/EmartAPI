from extensions import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class CartItem(db.Model, SerializerMixin):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    serialize_rules = ('-user.cart_items', '-product.cart_items',)

    products = db.relationship('Product', back_populates='cart_items', cascade="all, delete")



    @validates("quantity")
    def validate_quantity(self, key, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Quantity must be an integer greater than 0")
        return value
