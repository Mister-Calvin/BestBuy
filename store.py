from products import Product
from typing import List


class Store:
    """
    Initializes the Store with a list of Product objects.
    Args:
        product (list): A list of Product instances to be managed by the store.
    """
    def __init__(self, product):
        self.product = product #list of Products


    def add_product(self, products):
        """ Adds a list of Product instances to the store.
        Args: products (list): A list of Product instances to be added to the store."""
        self.product.append(products)


    def remove_product(self, products):
        """ Removes a list of Product instances from the store.
        Args: products (list): A list of Product instances to be removed from the store."""
        self.product.remove(products)


    def get_total_quantity(self) -> int:
        """ Returns the total quantity of the store."""
        total = 0
        for product in self.product:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> List[Product]:
        """ Returns a list of all products in the store."""
        products = []
        for product in self.product:
            if product.is_active():
                products.append(product)
        return products


    def order(self, shopping_list) -> float:
        """
        Processes an order for multiple products and quantities.
        Args:
            shopping_list (list of tuples): Each tuple contains a Product and the quantity to buy.
        Returns:
            float: The total price of the purchase.
        Raises:
            Exception: If a product cannot fulfill the requested quantity (handled by Product.buy).
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price



