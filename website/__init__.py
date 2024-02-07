from flask import Flask, send_from_directory
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_babel import Babel



db = SQLAlchemy()
DB_NAME = "database.db"
babel = Babel()
admin = Admin(template_mode='bootstrap3')
IMAGE_DIRECTORY = 'images' 
def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    babel.init_app(app)
    
    from .models import MyAdminIndexView, User, Registered_Unit, UserModelView
    admin.init_app(app, index_view=MyAdminIndexView())

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import initialize_admin_data
    
    # Add your model views here
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(ModelView(Registered_Unit, db.session))
    admin.add_link(MenuLink(name='Logout', url='/logout'))

    with app.app_context():
        db.create_all()  # Create tables based on models
        initialize_admin_data()  # Initialize admin data if needed

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "User needs to be logged in to view this page"
    login_manager.login_message_category = "error"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # Attempt to load a standard user
        return User.query.get(int(id))
    
    @app.route('/image/<filename>')
    def serve_image(filename):
        return send_from_directory(IMAGE_DIRECTORY, filename)

        
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all(app=app)
            print('Created Database!')
