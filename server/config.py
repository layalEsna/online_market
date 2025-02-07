# # Standard library imports
# # db.init_app(app)
# # Remote library imports
# from flask import Flask
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from flask_bcrypt import Bcrypt

# from dotenv import load_dotenv
# import os

# load_dotenv()
# # Local imports


# # Instantiate app, set attributes
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# # Define metadata, instantiate db
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# db = SQLAlchemy(metadata=metadata)
# migrate = Migrate(app, db)
# db.init_app(app)

# # Instantiate REST API
# api = Api(app)

# # Instantiate CORS
# CORS(app)

# bcrypt = Bcrypt(app)


# SECRET_KEY = os.getenv('SECRET_KEY')

# load_dotenv
# config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask import Flask
# ##### changes -> remove : from flask_cors import CORS move it to app.py
from flask_restful import Api
from sqlalchemy import MetaData
import os
####### from dotenv import load_dotenv -> move to app.py

######## load_dotenv() -> move to app.py

# Instantiate db, bcrypt, etc.
db = SQLAlchemy(metadata=MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}))
migrate = Migrate()
bcrypt = Bcrypt()
api = Api()


# app.config['SESSION_COOKIE_SAMESITE'] = 'None'
# app.config['SESSION_COOKIE_SECURE'] = False
# CORS = CORS
# CORS(app)
# Load your secret key and database URI
########SECRET_KEY = os.getenv('SECRET_KEY') since i have it in app.py

# ###### changes -> # CORS = CORS -> CORS(app) line 66
# ##### remove  CORS(app) add it in app.py

