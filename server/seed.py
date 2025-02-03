#!/usr/bin/env python3
# db.init_app(app)
# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from server import app
# from server.models import db

from server.models import db, User, Product, UserProduct

if __name__ == '__main__':
    fake = Faker()

    # Ensure the app context is pushed
    with app.app_context():
        print("Starting seed...")

        # Drop all tables (if you want to reset the database)
#         db.drop_all()

#         # Create all tables (based on models)
#         db.create_all()

#         # Adding users
#         for _ in range(5):
#             user = User(
#                 username=fake.user_name(),
#                 _hash_password=fake.password()  
#             )
#             db.session.add(user)

#         db.session.commit()

#         users = User.query.all()

#         # Adding products
#         for _ in range(10):
#             product = Product(
#                 name=fake.word(),
#                 description=fake.text(),
#                 price=round(randint(10, 1000) * 0.99, 2),
#                 user_id=rc(users).id  
#             )
#             db.session.add(product)

#         db.session.commit()

#         products = Product.query.all()

#         # Adding purchases
#         for _ in range(5):
#             purchase = Purchase(
#                 user_id=rc(users).id,  
#                 product_id=rc(products).id, 
#                 quantity=randint(1, 3),
#                 delivery_address=fake.address(),
#                 payment_method=rc(['Credit Card', 'Paypal', 'Cash on Delivery'])
#             )
#             db.session.add(purchase)

#         db.session.commit()

#         print("Seed data added successfully!")


# # #!/usr/bin/env python3

# # # Standard library imports
# # from random import randint, choice as rc

# # # Remote library imports
# # from faker import Faker

# # # Local imports
# # from app import app
# # from models import db

# # from models import User, Product, Purchase

# # if __name__ == '__main__':
# #     fake = Faker()
# #     with app.app_context():
# #         print("Starting seed...")
# #         # Seed code goes here!
