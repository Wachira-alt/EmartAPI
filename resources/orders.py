from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import CartItem, Order, OrderItem, Product
from extensions import db

class CheckoutResource(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        cart_items = CartItem.query.filter_by(user_id=user_id).all()
        if not cart_items:
            return {"error": "Cart is empty"}, 400

        order = Order(user_id=user_id)
        db.session.add(order)
        db.session.flush()  # So order.id is available

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=item.product.price  # snapshot price
            )
            db.session.add(order_item)
            db.session.delete(item)  # Clear from cart

        db.session.commit()
        return order.to_dict(), 201
