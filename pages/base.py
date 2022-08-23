from abc import ABCMeta

import selenium.webdriver.support.expected_conditions as EC
from locator import Locator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(metaclass=ABCMeta):
    """Абстрактный базовый класс для представления страниц"""
    def __init__(self, webdriver: WebDriver, timeout: float = 3) -> None:
        self._driver = webdriver
        self._timeout = timeout

    def expect_presence(self, locator: Locator) -> WebElement:
        """Ожидает либо появления элемента в DOM, либо истечения таймаута (бросая при этом `TimeoutException`)"""
        try:
            element = WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором {locator} не найден в DOM") from e

    def expect_visibility(self, locator: Locator) -> WebElement:
        """Ожидает либо видимости элемента на странице, либо истечения таймаута (бросая при этом `TimeoutException`)"""
        try:
            element = WebDriverWait(self._driver, self._timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором {locator} не виден на странице") from e

    def expect_invisibility(self, locator: Locator) -> WebElement:
        """Ожидает либо невидимости элемента на странице, либо истечения таймаута (бросая при этом `TimeoutException`)"""
        try:
            element = WebDriverWait(self._driver, self._timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором {locator} виден на странице") from e

    def expect_clickability(self, locator: Locator) -> WebElement:
        """Ожидает либо кликабельности элемента на странице, либо истечения таймаута (бросая при этом `TimeoutException`)"""
        element = self.expect_presence(locator)
        try:
            WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable(element)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором {locator} не кликабелен") from e
