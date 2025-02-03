#!/usr/bin/env python3
# db.init_app(app)
# Standard library imports
from random import randint, choice as rc

# from server.config import bcrypt
from server.config import bcrypt

# Remote library imports
from faker import Faker

# Local imports
from server import app
# from server.models import db

from decimal import Decimal


from server.models import db, User, Product, UserProduct

if __name__ == '__main__':
    fake = Faker()

    # Ensure the app context is pushed
    with app.app_context():
        print("Starting seed...")
        UserProduct.query.delete()
        Product.query.delete()
        User.query.delete()

        users = [
            User(username=fake.user_name(), _hash_password = bcrypt.generate_password_hash(fake.password()).decode('utf-8'))
            for _ in range(3)
        ]
        db.session.add_all(users)
        db.session.commit()
        print (f'Seeded {len(users)} users successfully!')

        products = [Product(
            name = fake.name(),
            description = fake.text(),
            image = fake.image_url(),
            price = Decimal(fake.random_number(digits=5))/Decimal('100.0'),
            
        )for _ in range(6)
        ]

        db.session.add_all(products)
        db.session.commit()
        print (f'Seeded {len(products)} products successfully!')
        
        user_products = [
            UserProduct(
                user_id = rc(users).id,
                product_id = rc(products).id,
                quantity = randint(1,4),
                delivery_address = fake.address(),
                payment_method = rc(['Credit Card', 'PayPal', 'Bank Transfer'])

            )
            for _ in range(6)
        ]

        db.session.add_all(user_products)
        db.session.commit()

        print (f'Seeded {len(user_products)} user_products successfully!')



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
