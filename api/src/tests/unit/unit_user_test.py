from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona')

        self.assertEqual(user.name, 'test',
                         "The name of the user after creation does not equal the constructor argument.")

        self.assertEqual(user.email, 'aaaa@aaa.it',
                         "The email of the user after creation does not equal the constructor argument.")

        self.assertEqual(user.birthdate, '12/12/2015',
                         "The birthdate of the user after creation does not equal the constructor argument.")

        self.assertEqual(user.address, '123 Barcelona',
                         "The address of the user after creation does not equal the constructor argument.")

    def test_user_json(self):
        user = UserModel('Jack', 'jack@aaa.com', '12/12/1965', '123 Miami')
        expected = {
            "name": "Jack",
            "email": "jack@aaa.com",
            "birthdate": "12/12/1965",
            "address": "123 Miami"
        }

        self.assertEqual(user.json(), expected,
                         "The JSON export of the user is incorrect. Received {}, expected {}.".format(user.json(),
                                                                                                      expected))
