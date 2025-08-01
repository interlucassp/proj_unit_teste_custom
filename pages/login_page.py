class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get("https://example.com/login")

    def login(self, username, password):
        self.driver.find_element("id", "user").send_keys(username)
        self.driver.find_element("id", "pass").send_keys(password)
        self.driver.find_element("id", "submit").click()
