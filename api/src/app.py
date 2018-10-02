import os

from flask import Flask
from flask_restful import Api

from resources.user import User, UserList

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)

api.add_resource(User, '/user/<string:name>')
api.add_resource(UserList, '/users')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host='0.0.0.0', port=5000)
