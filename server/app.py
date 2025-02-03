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
from flask import Flask
import os
from server.config import db, migrate, api, bcrypt
from server.models import *  # Import models to initialize them

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

if __name__ == '__main__':
    app.run(port=5555, debug=True)

