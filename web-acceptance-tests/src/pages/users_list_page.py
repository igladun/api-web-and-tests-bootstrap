from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UsersListPage(BasePage):
    TABLE_HEADER_NAME = By.ID, 'th_name'
    TABLE_HEADER_EMAIL = By.ID, 'th_email'
    TABLE_HEADER_BIRTHDAY = By.ID, 'th_bd'
    TABLE_HEADER_ADDRESS = By.ID, 'th_address'

    def get_table_header_name(self):
        return self.driver.find_element(*UsersListPage.TABLE_HEADER_NAME)

    def get_table_header_email(self):
        return self.driver.find_element(*UsersListPage.TABLE_HEADER_EMAIL)

    def get_table_header_birthday(self):
        return self.driver.find_element(*UsersListPage.TABLE_HEADER_BIRTHDAY)

    def get_table_header_address(self):
        return self.driver.find_element(*UsersListPage.TABLE_HEADER_ADDRESS)

    def check_user_exists(self, name, email, birthdate, address):
        return len(self.driver.find_elements_by_xpath(
            '//tr[ td[@id="tr_name"]="{}" and  td[@id="tr_email"]="{}" and  td[@id="tr_bd"]="{}" and  td[@id="tr_address"]="{}"  ]'.format(
                name, email, birthdate, address))) == 1
