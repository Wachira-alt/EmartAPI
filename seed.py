from app import create_app
from extensions import db
from models import User, Product, CartItem, Order, OrderItem

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Users
    admin = User(username="admin", email="admin@example.com", role="admin")
    admin.password_hash = "adminpass"

    user1 = User(username="john_doe", email="john@example.com")
    user1.password_hash = "johnspass"

    db.session.add_all([admin, user1])
    db.session.commit()

    # Create Products
    product1 = Product(title="Custom Notebook", description="A5 ruled pages", price=450.00, stock=100)
    product2 = Product(title="Branded Pen", description="Blue ink", price=150.00, stock=200)

    db.session.add_all([product1, product2])
    db.session.commit()

    # CartItem for user1
    cart1 = CartItem(user_id=user1.id, product_id=product1.id, quantity=2)
    cart2 = CartItem(user_id=user1.id, product_id=product2.id, quantity=3)

    db.session.add_all([cart1, cart2])
    db.session.commit()

    # Create an order for user1
    order = Order(user_id=user1.id, status='completed')
    db.session.add(order)
    db.session.commit()

    order_item1 = OrderItem(order_id=order.id, product_id=product1.id, quantity=2, price_at_purchase=450.00)
    order_item2 = OrderItem(order_id=order.id, product_id=product2.id, quantity=3, price_at_purchase=150.00)

    db.session.add_all([order_item1, order_item2])
    db.session.commit()

    print("🌱 Database seeded successfully!")
