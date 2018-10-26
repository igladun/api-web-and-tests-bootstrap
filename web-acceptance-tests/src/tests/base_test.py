from selenium import webdriver
from unittest import TestCase


class BaseTest(TestCase):
    IMPLICIT_WAIT = 10

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(BaseTest.IMPLICIT_WAIT)

    def tearDown(self):
        self.driver.quit()
