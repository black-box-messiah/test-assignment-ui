from typing import Iterable
from selenium.webdriver.common.by import By


class Locator:
    """Сущность для представления локаторов в коде."""
    def __init__(self, type: By, query: str) -> None:
        self._type = type
        self._query = query

    @classmethod
    def from_XPath(cls, xpath: str) -> "Locator":
        """Создаёт локатор по XPath"""
        return cls(By.XPATH, xpath)

    @classmethod
    def from_css(cls, selector: str) -> "Locator":
        """Создаёт локатор по CSS селектору"""
        return cls(By.CSS_SELECTOR, selector)

    def __iter__(self) -> Iterable:
        yield self._type
        yield self._query

    def __add__(self, other) -> "Locator":
        if isinstance(other, str):
            return Locator(self._type, self._query + other)
        elif isinstance(other, Locator):
            if (self._type != other._type):
                raise ValueError("Locator можно складывать только с Locator того же типа")
            return Locator(self._type, self._query + other._query)
        else:
            raise TypeError("Locator можно складывать только с Locator или строкой")

    def __repr__(self):
        return f"Locator({repr(self._type)}, {repr(self._query)})"
