import os

from selenium import webdriver
from unittest import TestCase


class BaseTest(TestCase):
    TEST_URL = os.environ.get('web-service:80', 'localhost:5005')
    USER_LIST_URL = TEST_URL + '/list'
    CREATE_USER_URL = TEST_URL + '/create'


    IMPLICIT_WAIT = 30

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(BaseTest.IMPLICIT_WAIT)

    def tearDown(self):
        self.driver.quit()
