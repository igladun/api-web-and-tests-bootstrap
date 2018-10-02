from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_and_delete(self):
        with self.app_context():

            user = UserModel('test', 'aaaa@aaa.it', '12/12/2015', '123 Barcelona')

            self.assertIsNone(UserModel.find_by_name('test'), "Found an user with name 'test' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_name('test'),
                                 "Did not find an user with name 'test' after save_to_db")

            user.delete_from_db()

            self.assertIsNone(UserModel.find_by_name('test'), "Found an user with name 'test' after delete_from_db")

