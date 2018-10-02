from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateUserPage(BasePage):
    FIELD_NAME = By.NAME, 'name'
    FIELD_EMAIL = By.NAME, 'email'
    FIELD_BIRTHDATE = By.NAME, 'birthdate'
    FIELD_ADDRESS = By.NAME, 'address'

    def get_field_name(self):
        return self.driver.find_element(*CreateUserPage.FIELD_NAME)

    def get_field_email(self):
        return self.driver.find_element(*CreateUserPage.FIELD_EMAIL)

    def get_field_birthdate(self):
        return self.driver.find_element(*CreateUserPage.FIELD_BIRTHDATE)

    def get_field_address(self):
        return self.driver.find_element(*CreateUserPage.FIELD_ADDRESS)
