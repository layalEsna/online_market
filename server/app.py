# #!/usr/bin/env python3

# # Standard library imports
# # db.init_app(app)
# # Remote library imports
# from flask import request
# from flask_restful import Resource

# # Local imports
# from .config import app, db, api, migrate
# # Add your model imports



# # Views go here!

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


# app.py
from flask import Flask, request, make_response, jsonify, session
from flask_restful import Resource
import os
from server.config import db, migrate, api, bcrypt
from server.models import *  

app = Flask(__name__)

# App config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/layla/Development/code/se-prep/phase-4/online_market/server/instance/app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize db, migrate, and api
db.init_app(app)
migrate.init_app(app, db)
api.init_app(app)

# Start your views and routes
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

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

        
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

