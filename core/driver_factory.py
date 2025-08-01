from selenium import webdriver

def create_driver(browser="chrome"):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise Exception("Browser not supported.")
