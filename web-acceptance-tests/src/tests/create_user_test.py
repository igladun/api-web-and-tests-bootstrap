from pages.create_user_page import CreateUserPage
from pages.results_page import ResultsPage
from pages.users_list_page import UsersListPage
from tests.base_test import BaseTest
from random import randint


class CreateUserTest(BaseTest):
    def setUp(self):
        super(CreateUserTest, self).setUp()
        CreateUserPage.go_to_page(self)

    def test_title(self):
        create_user_page = CreateUserPage(self.driver)
        self.assertEqual(create_user_page.title, 'Create User')

    def test_form_inputs_exist(self):
        create_user_page = CreateUserPage(self.driver)
        create_user_page.check_inputs()

    def test_create_user(self):
        test_user = 'igr' + str(randint(0, 100000))

        create_user_page = CreateUserPage(self.driver)
        create_user_page.enter_user_info(test_user, 'i@i.com', '10/10/2000', '444')
        results_page = ResultsPage(self.driver)
        self.assertEqual(results_page.message_text, 'User {} created'.format(test_user))

        create_user_page.go_to_page(self)
        users_page = UsersListPage(self.driver)
        self.assertTrue(users_page.check_user_exists(test_user, 'i@i.com', '10/10/2000', '444'))

    def test_create_duplicate_user(self):
        test_user = 'igr' + str(randint(0, 100000))

        create_user_page = CreateUserPage(self.driver)
        results_page = create_user_page.enter_user_info(test_user, 'i@i.com', '10/10/2000', '444')
        self.assertEqual(results_page.message_text, 'User {} created'.format(test_user))

        create_user_page.go_to_page(self)
        results_page = create_user_page.enter_user_info(test_user, 'i@i.com', '10/10/2000', '444')
        self.assertEqual(results_page.message_text, 'A user with name {} already exists.'.format(test_user))
