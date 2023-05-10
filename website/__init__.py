from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path


db = SQLAlchemy()
mozarstore = "database.db"


def create_app():
    app = Flask(__name__)
    # adding database
    app.config['SECRET_KEY'] = 'jasonleomozar'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{mozarstore}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + mozarstore):
        with app.app_context():
            db.create_all()
        print('Created Database!')

if __name__ == '__main__':
    db.create_all()
    app.run()
