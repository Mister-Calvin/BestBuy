class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not name:
            raise Exception("Name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity:{self.quantity}")


    def buy(self, quantity) -> float:
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("not enough available")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity
