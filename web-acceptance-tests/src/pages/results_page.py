from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResultsPage(BasePage):
    TEXT_MESSAGE = By.ID, 'message'

    def get_message(self):
        return self.driver.find_element(*ResultsPage.TEXT_MESSAGE)

    @property
    def message_text(self):
        return self.get_message().text


