import os

from flask import Flask, render_template, request

from models.user import UserModel

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')



@app.route('/list')
def user_list():
    users = [x.json() for x in UserModel.query.all()]
    return render_template('users.html', users=users)


@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.form

        if UserModel.find_by_name(request.form['name']):
            return 'A user with name {} already exists.'.format(data['name']), 400

        user = UserModel(name=data['name'],
                         email=data['email'],
                         birthdate=data['birthdate'],
                         address=data['address'],
                         )
        try:
            user.save_to_db()
        except:
            return 'An error occured while createing the user', 500

        return 'User {} created'.format(request.form['name']), 201
    else:
        return render_template('create.html')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host='0.0.0.0', port=80)
