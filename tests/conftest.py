import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def webdriver_options() -> ChromeOptions:
    return ChromeOptions()


@pytest.fixture
def webdriver(webdriver_options) -> WebDriver:
    with Chrome(options=webdriver_options) as driver:
        yield driver
