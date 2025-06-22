from app import create_app
from extensions import db
from models import User, Product, CartItem, Order

app = create_app()

with app.app_context():
    print("Seeding database...")

    # Clear tables first
    CartItem.query.delete()
    Order.query.delete()
    Product.query.delete()
    User.query.delete()

    # Create users
    admin = User(username="admin", email="admin@elimu.com", role="admin")
    admin.password_hash = "adminpass"

    user = User(username="john", email="john@elimu.com")
    user.password_hash = "johnpass"

    db.session.add_all([admin, user])
    db.session.commit()

    # Create products
    p1 = Product(title="A4 Notebook", description="Lined A4 notebook", price=350.0, stock=50)
    p2 = Product(title="Ballpoint Pen", description="Blue ink pen", price=50.0, stock=200)
    p3 = Product(title="Stapler", description="Heavy-duty stapler", price=750.0, stock=30)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Add cart items
    cart_item = CartItem(user_id=user.id, product_id=p1.id, quantity=2)
    db.session.add(cart_item)

    db.session.commit()

    print("✅ Done seeding!")
