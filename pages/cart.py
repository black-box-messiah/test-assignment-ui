import allure
from entities.product_stack import ProductStack
from locator import Locator
from selenium.webdriver.remote.webdriver import WebDriver

from .base import BasePage


class CartPage(BasePage):

    _first_cart_item = Locator.from_css(".basket-product-item:nth-child(1)")
    _first_cart_item_name = _first_cart_item + " *[data-test-id='product-title']"
    _first_cart_item_amount = _first_cart_item + " *[data-test-id='product-input-count']"
    _first_cart_item_price = _first_cart_item + " *[data-test-id='product-price']"

    def __init__(self, webdriver: WebDriver) -> None:
        super().__init__(webdriver)

    @allure.step("Получить информацию о первом продукте в корзине")
    def get_first_item_info(self) -> ProductStack:
        return ProductStack(
            name=self.get_first_item_name(),
            price=self.get_first_item_price(),
            amount=int(self.get_first_item_amount()),
        )

    @allure.step("Получить наименование первого продукта в корзине")
    def get_first_item_name(self) -> str:
        element = self.expect_visibility(self._first_cart_item_name)
        return element.text

    @allure.step("Получить количество первого продукта в корзине")
    def get_first_item_amount(self) -> str:
        element = self.expect_visibility(self._first_cart_item_amount)
        return str(element.get_attribute("value"))

    @allure.step("Получить цену первого продукта в корзине")
    def get_first_item_price(self) -> str:
        element = self.expect_visibility(self._first_cart_item_price)
        return element.text
