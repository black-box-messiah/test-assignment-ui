import allure
from locator import Locator
from selenium.webdriver.remote.webdriver import WebDriver

from .base import BasePage


class MainPage(BasePage):
    """Главная страница сайта"""
    _first_product = Locator.from_XPath("//*[contains(concat(' ', @class, ' '), 'product-card')][1]")

    @allure.step("Перейти на главную страницу сайта")
    def navigate(self) -> None:
        self._driver.get("https://apteka.magnit.ru/")

    @allure.step("Кликнуть на первый товар")
    def click_first_product(self) -> None:
        element = self.expect_visibility(self._first_product)
        element.click()
