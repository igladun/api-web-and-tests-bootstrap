class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title
