from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:

        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} is not in the store.")

            total_price += product.buy(quantity)

        return total_price

if __name__ == "__main__":
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    store = Store([mac, bose])

    store.add_product(pixel)

    print(store.get_total_quantity())

    products = store.get_all_products()
    for product in products:
        print(product.show())

    shopping_list = [(mac, 2), (bose, 5)]
    total_price = store.order(shopping_list)
    print(f"Order cost: {total_price} dollars.")
