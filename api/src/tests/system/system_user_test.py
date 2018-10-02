from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def setUp(self):
        super(UserTest, self).setUp()

    def test_user_not_found(self):
        with self.app() as client:
            response = client.get('/user/test')
            self.assertEqual(response.status_code, 404)
            self.assertDictEqual({'message': 'User not found'},
                                 json.loads(response.data))

    def test_user_found(self):
        with self.app() as c:
            with self.app_context():
                UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona').save_to_db()
                response = c.get('/user/test')
                expected = {
                    "name": "test",
                    "email": "aaaa@aaa.it",
                    "birthdate": "12/12/2015",
                    "address": "123 Barcelona"
                }

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(expected, json.loads(response.data))

    def test_create_user(self):
        with self.app() as c:
            with self.app_context():
                expected = {
                    "name": "Tom",
                    "email": "tom@tomtom.com",
                    "birthdate": "Jan 11 1912",
                    "address": "12345 NYC"
                }
                response = c.post('/user/Tom', headers={'Content-Type': 'application/json'}, data=json.dumps(expected))

                self.assertEqual(response.status_code, 201)

                self.assertEqual(UserModel.find_by_name('Tom').email, 'tom@tomtom.com')

                self.assertEqual(UserModel.find_by_name('Tom').birthdate, 'Jan 11 1912')

                self.assertEqual(UserModel.find_by_name('Tom').address, '12345 NYC')

                self.assertDictEqual(expected, json.loads(response.data))

    def test_create_duplicate_user(self):
        with self.app() as c:
            with self.app_context():
                with self.app_context():
                    expected = {
                        "name": "Tom",
                        "email": "tom@tomtom.com",
                        "birthdate": "Jan 11 1912",
                        "address": "12345 NYC"
                    }
                response = c.post('/user/Tom', headers={'Content-Type': 'application/json'}, data=json.dumps(expected))
                self.assertEqual(response.status_code, 201)

                response = c.post('/user/Tom', headers={'Content-Type': 'application/json'}, data=json.dumps(expected))
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'A user with name \'Tom\' already exists.'},
                                     json.loads(response.data))


    def test_user_list(self):
        with self.app() as c:
            with self.app_context():
                UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona').save_to_db()
                UserModel('test2', 'bbbb@cccc.app', '05/06/2013', '123 London').save_to_db()

                response = c.get('/users')

                expected = {'users': [
                    {'address': '123 Barcelona',
                     'birthdate': '12/12/2015',
                     'email': 'aaaa@aaa.it',
                     'name': 'test'},
                    {'address': '123 London',
                     'birthdate': '05/06/2013',
                     'email': 'bbbb@cccc.app',
                     'name': 'test2'}]}

                actual_result = json.loads(response.data)

                self.assertDictEqual(expected, actual_result)
                self.assertEqual(len(actual_result['users']), 2, 'Incorrect number of users are returned')
                self.assertEqual(response.status_code, 200)
