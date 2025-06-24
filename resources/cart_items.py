# from flask_restful import Resource
# from flask import request
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from models import CartItem, Product
# from extensions import db

# class CartItemListResource(Resource):
#     @jwt_required()
#     def get(self):
#         user_id = get_jwt_identity()
#         items = CartItem.query.filter_by(user_id=user_id).all()
#         return [item.to_dict() for item in items], 200

#     @jwt_required()
#     def post(self):
#         data = request.get_json()
#         product_id = data.get("product_id")
#         quantity = data.get("quantity", 1)
#         user_id = get_jwt_identity()

#         # Check if already exists
#         existing = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
#         if existing:
#             existing.quantity += quantity
#         else:
#             new_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
#             db.session.add(new_item)

#         db.session.commit()
#         return {"message": "Cart updated"}, 201

# class CartItemDetailResource(Resource):
#     @jwt_required()
#     def patch(self, id):
#         data = request.get_json()
#         item = CartItem.query.get_or_404(id)
#         item.quantity = data.get("quantity", item.quantity)
#         db.session.commit()
#         return item.to_dict(), 200

#     @jwt_required()
#     def delete(self, id):
#         item = CartItem.query.get_or_404(id)
#         db.session.delete(item)
#         db.session.commit()
#         return {"message": "Item removed"}, 204
