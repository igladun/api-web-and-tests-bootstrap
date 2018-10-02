from pages.create_user_page import CreateUserPage
from tests.base_test import BaseTest


class CreateUserTest(BaseTest):

    def setUp(self):
        super(CreateUserTest, self).setUp()
        self.driver.get(BaseTest.CREATE_USER_URL)

    def test_title(self):
        create_user_page = CreateUserPage(self.driver)
        self.assertEqual(create_user_page.title, 'Create User')

    def test_form_inputs_exist(self):
        create_user_page = CreateUserPage(self.driver)
        self.assertTrue(create_user_page.get_field_name().is_displayed())
        self.assertTrue(create_user_page.get_field_email().is_displayed())
        self.assertTrue(create_user_page.get_field_birthdate().is_displayed())
        self.assertTrue(create_user_page.get_field_address().is_displayed())

