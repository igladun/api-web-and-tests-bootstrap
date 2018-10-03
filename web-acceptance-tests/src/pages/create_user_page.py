from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CreateUserPage(BasePage):
    FIELD_NAME = By.NAME, 'name'
    FIELD_EMAIL = By.NAME, 'email'
    FIELD_BIRTHDATE = By.NAME, 'birthdate'
    FIELD_ADDRESS = By.NAME, 'address'
    BUTTON_SUBMIT = By.ID , 'sub_but'

    def get_field_name(self):
        return self.driver.find_element(*CreateUserPage.FIELD_NAME)

    def get_field_email(self):
        return self.driver.find_element(*CreateUserPage.FIELD_EMAIL)

    def get_field_birthdate(self):
        return self.driver.find_element(*CreateUserPage.FIELD_BIRTHDATE)

    def get_field_address(self):
        return self.driver.find_element(*CreateUserPage.FIELD_ADDRESS)


    def get_submit_button(self):
        return self.driver.find_element(*CreateUserPage.BUTTON_SUBMIT)

    def enter_user_info(self, name, email, birthdate, address):
        self.get_field_name().send_keys(name)
        self.get_field_email().send_keys(email)
        self.get_field_birthdate().send_keys(birthdate)
        self.get_field_address().send_keys(address)
        self.get_submit_button().click()


