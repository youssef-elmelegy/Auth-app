from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    CORS(app, origins="http://localhost:5173", supports_credentials=True)
    app.config['SECRET_KEY'] = 'password'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    app.url_map.strict_slashes = False  ## This line is not necessary just for handling trailing slashes
    
    from .routes.auth import auth_bp
    
    app.register_blueprint(auth_bp, url_prefix='/')
    
    from  .models import User
    create_database(app)
        
    return app

def create_database(app):
    with app.app_context():
        if not path.exists( 'website/' + DB_NAME):
            db.create_all()
            print('Created Database!')