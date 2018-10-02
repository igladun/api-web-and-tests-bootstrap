from flask_restful import Resource, request
from models.user import UserModel


class User(Resource):
    def get(self, name):
        user = UserModel.find_by_name(name)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self, name):
        if UserModel.find_by_name(name):
            return {'message': "A user with name '{}' already exists.".format(name)}, 400

        data = request.get_json()

        # user = UserModel(name = data['name'],
        #                  email = data['email'],
        #                  birthdate  = datetime.strptime(data['birthdate'], '%b %d %Y'),
        #                  address= data['address'],
        #                  )

        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500

        return user.json(), 201



class UserList(Resource):
    def get(self):
        return {'users': [x.json() for x in UserModel.query.all()]}
