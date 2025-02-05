# load_dotenv
# CORS = CORS
# app.py
from flask import Flask, request, make_response, jsonify, session
from flask_restful import Resource
from dotenv import load_dotenv
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

       
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Sellers, '/sellers')
print("Route /sellers has been added!")

api.init_app(app)


if __name__ == '__main__':
    print("Flask server is starting...")
    app.run(port=5555, debug=True)

