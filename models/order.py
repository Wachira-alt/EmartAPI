from extensions import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')
    items_json = db.Column(db.Text)  # Save cart snapshot

    serialize_rules = ('-user.orders',)
