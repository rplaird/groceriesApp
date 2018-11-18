from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_page_routes(app):
    
    @app.route('/members')
    def members():
        return render_template('members.html')
    
    @app.route('/families')
    def families():
        return render_template('families.html')
        
    @app.route('/users')
    def users():
        return render_template('users.html')
            
    @app.route('/admin')
    def admin():
        return render_template('admin.html')
        
    @app.route('/login')
    def login():
        return render_template('login.html')
        
    @app.route('/test')
    def test():
        return app.send_static_file('./login/index.html')
        
    @app.route('/home')
    def home():
        return render_template('home.html')

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)  

    return app