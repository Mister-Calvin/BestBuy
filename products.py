class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance.
        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The available quantity in stock. Must be non-negative.
        Raises:
            Exception: If any of the input values are invalid.
        """
        if not name:
            raise Exception("Name is required")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """
        Returns the current available quantity of the product.
        Returns:
            int: The quantity in stock.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets a new quantity for the product.
        If the quantity is set to zero, the product is deactivated.
        Args:
            quantity (int): The new quantity to set.
        Raises:
            ValueError: If the quantity is negative.
        """
        self.quantity = quantity
        if self.quantity == 0:
            return self.deactivate()


    def is_active(self) -> bool:
        """
        Checks whether the product is active.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """Activates the product, setting its active status to True."""
        self.active = True


    def deactivate(self):
        """Deactivates the product, setting its active status to False."""
        self.active = False

    def show(self, index=None):
        """
        Prints a summary of the product, including its name, price, and quantity.
        Optionally includes an index number for display purposes.

        Args:
            index (int, optional): The product's index in a list (1-based display).
        """
        if index is not None:
            print(f"{index}. {self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        """
        Processes the purchase of a given quantity of the product.
        Args:
            quantity (int): The quantity to purchase.
        Returns:
            float: The total price for the purchase.
        Raises:
            Exception: If the requested quantity is invalid or exceeds available stock.
        """
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("not enough available")


        self.quantity = self.quantity - quantity
        if self.quantity == 0:
            self.deactivate()
        total_price = quantity * self.price
        return total_price

