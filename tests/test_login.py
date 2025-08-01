import pytest
from pages.login_page import LoginPage
from core.driver_factory import create_driver

@pytest.fixture
def driver():
    d = create_driver()
    yield d
    d.quit()

def test_valid_login(driver):
    page = LoginPage(driver)
    page.visit()
    page.login("admin", "admin123")
    assert "Dashboard" in driver.title
