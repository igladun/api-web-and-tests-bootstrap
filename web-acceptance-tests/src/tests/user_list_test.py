from pages.users_list_page import UsersListPage
from tests.base_test import BaseTest


class UserListTest(BaseTest):
    def setUp(self):
        super(UserListTest, self).setUp()
        UsersListPage.go_to_page(self)

    def test_title(self):
        users_page = UsersListPage(self.driver)
        self.assertEqual(users_page.title, 'User list')

    def test_table_headers(self):
        users_page = UsersListPage(self.driver)
        self.assertEqual(users_page.get_table_header_name().text, 'Name')
        self.assertEqual(users_page.get_table_header_email().text, 'Email')
        self.assertEqual(users_page.get_table_header_birthday().text, 'Birthdate')
        self.assertEqual(users_page.get_table_header_address().text, 'Address')
