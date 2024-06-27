from abc import ABC, abstractmethod

class ProductStrategy(ABC):
    @abstractmethod
    def search_product(self, query):
        pass

    @abstractmethod
    def display_product(self):
        pass

    @abstractmethod
    def order_product(self, quantity):
        pass

class Product:
    def __init__(self, name, price, type, strategy: ProductStrategy):
        self.name = name
        self.price = price
        self.type = type
        self.strategy = strategy

    def search_product(self, query):
        return self.strategy.search_product(query)

    def display_product(self):
        return self.strategy.display_product()

    def order_product(self, quantity):
        return self.strategy.order_product(quantity)

class ConcreteProductStrategy(ProductStrategy):
    def search_product(self, query):
        # Реалізація пошуку товару за запитом
        pass

    def display_product(self):
        # Реалізація відображення інформації про товар
        pass

    def order_product(self, quantity):
        # Реалізація замовлення товару
        pass


product = Product("Smartphone", 500, "Electronics", ConcreteProductStrategy())
product.search_product("smartphone")
product.display_product()
product.order_product(1)