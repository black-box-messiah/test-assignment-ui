import allure
from pages.cart import CartPage
from pages.main import MainPage
from pages.product import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.feature("Корзина")
class TestCart():
    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_to_cart(self, webdriver: WebDriver):
        main_page = MainPage(webdriver)
        main_page.navigate()
        main_page.click_first_product()

        product_page = ProductPage(webdriver)
        product_info = product_page.get_product_info()
        product_page.click_button_add_to_cart()

        product_page.check_button_add_to_cart_invisible()
        product_page.check_product_amount_input_visible()
        assert int(product_page.get_cart_counter_text()) == product_info.amount

        product_page.click_header_cart()
        
        cart_page = CartPage(webdriver)
        cart_item_info = cart_page.get_first_item_info()
        assert cart_item_info == product_info, "Данные о товаре в корзине и на странице товара не совпадают"
