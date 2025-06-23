from flask_restful import Api
from flask import Blueprint
from .auth import RegisterResource, LoginResource, ProfileResource
from .products import ProductListResource, ProductDetailResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Auth routes
api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
api.add_resource(ProfileResource, "/profile")

#product endpoints

api.add_resource(ProductListResource, "/products")
api.add_resource(ProductDetailResource, "/products/<int:id>")

