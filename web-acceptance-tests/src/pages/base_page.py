import os


class BasePage:
    if os.environ.get('INSIDE_DOCKER', False):
        TEST_URL = 'http://web-service:80'
    else:
        TEST_URL = 'http://localhost:5005'

    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title
