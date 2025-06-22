from extensions import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String)
    stock = db.Column(db.Integer, default=0)

    cart_items = db.relationship('CartItem', backref='product', cascade="all, delete")

    serialize_rules = ('-cart_items.product',)

    @validates("price")
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price must be positive")
        return value

    @validates("title")
    def validate_title(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Title must be at least 2 characters long")
        return value
