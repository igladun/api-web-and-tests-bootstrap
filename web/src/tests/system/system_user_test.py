from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def setUp(self):
        super(UserTest, self).setUp()


    def test_users_list_http_code(self):
        with self.app() as c:
            with self.app_context():
                UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona').save_to_db()
                response = c.get('/list')
                self.assertEqual(response.status_code, 200)


    def test_create_user_http_code(self):
        with self.app() as c:
            with self.app_context():
                UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona').save_to_db()
                response = c.get('/list')
                self.assertEqual(response.status_code, 200)
