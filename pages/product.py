import allure
from entities.product_stack import ProductStack
from locator import Locator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from .base import BasePage


class ProductPage(BasePage):
    """Страница конкретного товара"""

    _product_main_info = Locator.from_XPath("//*[contains(concat(' ', @class, ' '), 'product-page__main')]")

    _product_name = Locator.from_XPath("//*[@data-test-id='page-title']")
    _product_price = _product_main_info + "//*[@data-test-id='product-price']"
    _product_amount_selected = _product_main_info + "//*[@data-test-id='product-input-count']"

    _button_add_to_cart = _product_main_info + "//*[@data-test-id='product-buy-btn']"

    _product_amount_input = Locator.from_css(".count__wrapper")

    _header_cart = Locator.from_css("*[data-test-id='small-cart']")
    _header_cart_counter = _header_cart + " .b-counter"

    @allure.step("Получить наименование товара")
    def get_product_name(self) -> str:
        element = self.expect_visibility(self._product_name)
        return element.text

    @allure.step("Получить цену товара")
    def get_product_price(self) -> str:
        element = self.expect_visibility(self._product_price)
        return element.text

    @allure.step("Получить выбранное количество товара")
    def get_product_amount_selected(self) -> str:
        element = self.expect_visibility(self._product_amount_selected)
        return element.get_attribute("value")

    @allure.step("Получить информацию о товаре")
    def get_product_info(self) -> ProductStack:
        return ProductStack(
            name=self.get_product_name(),
            price=self.get_product_price(),
            amount=int(self.get_product_amount_selected())
        )

    @allure.step("Получить информацию о количестве товаров в корзине")
    def get_cart_counter_text(self) -> str:
        element = self.expect_visibility(self._header_cart_counter)
        return element.text

    @allure.step("Проверить невидимость кнопки \"Добавить в корзину\"")
    def check_button_add_to_cart_invisible(self) -> None:
        self.expect_invisibility(self._button_add_to_cart)

    @allure.step("Проверить видимость поля с количеством товара")
    def check_product_amount_input_visible(self) -> None:
        self.expect_visibility(self._product_amount_input)

    @allure.step("Кликнуть по кнопке \"Добавить в корзину\"")
    def click_button_add_to_cart(self) -> None:
        element = self.expect_clickability(self._button_add_to_cart)
        element.click()

    @allure.step("Кликнуть по корзине в хэдере")
    def click_header_cart(self) -> None:
        element = self.expect_clickability(self._header_cart)
        element.click()
