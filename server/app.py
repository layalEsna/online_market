# load_dotenv
# CORS = CORS
# app.py
from flask import Flask, request, make_response, jsonify, session
from flask_restful import Resource
from dotenv import load_dotenv


# ############  add from flask_session import Session
from flask_session import Session


import os
load_dotenv()
from server.config import db, migrate, api, bcrypt
from server.models import *  

######
from flask_cors import CORS

app = Flask(__name__)

######
######CORS(app) -> replace with
######CORS(app, resources={r"/api/*": {"origins": "*"}}) -> replace with
CORS(app, supports_credentials=True)




app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True  # Secure cookies
app.config['SESSION_FILE_DIR'] = './flask_session'  # Store session files locally
Session(app)  # <-- Initialize Flask-Session



#########add app.config['SESSION_COOKIE_SAMESITE'] = 'None'
##########app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = False





# App config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/layla/Development/code/se-prep/phase-4/online_market/server/instance/app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize db, migrate, and api
db.init_app(app)
migrate.init_app(app, db)
# api.init_app(app)

# Start your views and routes 
@app.route('/')
def index():
    return '<h1>Project Server here</h1>'

@app.before_request
def print_session():
    print("SESSION CONTENTS:", session)


class Signup(Resource):
    def post(self):

        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            if not all([username, password, confirm_password ]):
                return make_response(jsonify({'error': 'All the fields are required.'}), 400)
            if password != confirm_password:
                return make_response(jsonify({'error': 'Password not match.'}), 401)
            if User.query.filter(User.username==username).first():
                return make_response(jsonify({'error': 'Username already exists.'}), 401)
            
            new_user = User(
                username = username,
                password = password
            )

            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id

            session['user_id']

            return make_response(jsonify(new_user.to_dict()), 201)

        except Exception as e:
            return make_response(jsonify({'error': f'Internal error: {e}'}), 500)
        
class Login(Resource):
    def post(self):

        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            if not all([username, password]):
                return make_response(jsonify({'error': 'All the fields are required.'}),400)
            user = User.query.filter(User.username==username).first()
            if not user or not user.check_password(password):
                return make_response(jsonify({'error': 'Wrong username or password.'}), 404)
            
            session['user_id'] = user.id

            print("SESSION CONTENTS AFTER LOGIN:", session) 

            return make_response(jsonify({'message': 'Successful login!'}), 200)

        except Exception as e:
            return make_response(jsonify({'error': f'Internal error: {e}'}), 500)
        
class Sellers(Resource):
    def get(self):
        print("Sellers endpoint was hit!")

        sellers = User.query.all()
        if not sellers:
            return make_response(jsonify({'count': 0, 'sellers': []}), 200)

        sellers_with_products = [
            {
                'id': seller.id,
                'username': seller.username,
                'products': [
                    {
                        'id': product.product.id,
                        'name': product.product.name,
                        'description': product.product.description,
                        'image': product.product.image,
                        'price': product.product.price
                    }
                    for product in seller.user_products
                ]            
            }
             for seller in sellers
        ]

        return make_response(jsonify({'count': len(sellers_with_products), 'sellers': sellers_with_products}), 200)

class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id==id).first()
        if not product:
            return make_response(jsonify({'error': f'Product with ID: {id} not found.'}), 404)
        return make_response(jsonify(product.to_dict()), 200)
    
class Purchase(Resource):
    def post(self, product_id):

        print("Received session cookie:", request.cookies.get("session"))  # Debugging
        print("Session contents during purchase:", dict(session))  # Debugging


        data = request.get_json()
        quantity = data.get('quantity')
        delivery_address = data.get('delivery_address')
        payment_method = data.get('payment_method')
        user_id = session.get('user_id')
        print("SESSION CONTENTS DURING PURCHASE:", session)

        if not user_id:
            return make_response(jsonify({'error': 'User must be logged in to make a purchase.'}), 401)

        if not all([quantity, delivery_address, payment_method]):
            return make_response(jsonify({'error': 'All the fields are required.'}), 400)
        if len(delivery_address) > 255:
            return make_response(jsonify({'error': 'Delivery address must be shorter than 255 characters.'}), 401)
        new_purchase = UserProduct(
            user_id = user_id,
            quantity = quantity,
            delivery_address = delivery_address,
            payment_method = payment_method,
            product_id=product_id,
        )

        db.session.add(new_purchase)
        db.session.commit()

        session['purchase_id'] = new_purchase.id

        return make_response(jsonify(new_purchase.to_dict()), 201)

class Cart(Resource):
    def get(self):

        purchases = UserProduct.query.all()
        if not purchases:
            return make_response(jsonify({'count': 0, 'cart': []}), 200)
        
        cart_items = [
            {
                'id': purchase.id,
                'user_id': purchase.user_id,

                'product': {
                    'id': purchase.product.id,
                    'name': purchase.product.name,
                    'description': purchase.product.description,
                    'image': purchase.product.image,
                    'price': purchase.product.price,
                },
                'quantity': purchase.quantity,
                'delivery_address': purchase.delivery_address,
                'payment_method': purchase.payment_method,
            }
            for purchase in purchases
        ]

        return make_response(jsonify({'count': len(cart_items), 'cart': cart_items}), 200)
               
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Sellers, '/sellers')
api.add_resource(ProductById, '/products/<int:id>')
api.add_resource(Purchase, '/products/<int:product_id>/purchase')
api.add_resource(Cart, '/products/purchases')

print("Route /sellers has been added!")

api.init_app(app)


if __name__ == '__main__':
    print("Flask server is starting...")
    app.run(port=5555, debug=True)

