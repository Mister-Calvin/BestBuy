from products import Product
from store import Store

# setup initial stock of inventory
def input_products():
    """Creates and returns a predefined list of initial Product instances.

        Returns:
            list: A list of Product objects to be used as initial store inventory."""
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     Product("Google Pixel 7", price=500, quantity=250)
                   ]
    return product_list


def make_object():
    """Initializes a Store object using the predefined product list.

        Returns:
            Store: A Store instance containing the initial set of products."""
    best_buy = Store(input_products())
    return best_buy


def products_list():
    """Retrieves all active products currently in the store.

    Returns:
        list: A list of active Product objects."""
    products = make_object().get_all_products() #list
    return products


def show_products():
    """Displays all active products in the store with their index, name, price, and quantity."""
    for index, product in enumerate(products_list()):
        print(f"{index + 1}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


def show_quantities():
    """Calculates and prints the total quantity of all products in the store."""
    total_quantity = 0
    for product in products_list():
        total_quantity += product.get_quantity()
    print(f"Total of {total_quantity} in Store")


def make_order():
    """Allows the user to create an order by selecting products and specifying quantities.
        The user can add multiple products, and the total price is displayed at the end.
        Pressing Enter without input finalizes the order."""
    order = []
    show_products()
    while True:
        which_product_input = input("Which product do you want to buy: \n(leave blank for checkout)")
        if which_product_input == "":
            break
        which_product = int(which_product_input)

        which_quantity_input = int(input("Which quantity do you want to buy: "))
        selected_product = products_list()[which_product-1]
        order.append((selected_product, which_quantity_input))
        print("Product added to list!\n")
    print(f"Order made! Total payment: {make_object().order(order)}")



def menu():
    """Displays the main menu and handles user input to interact with the store system.
        Options:
        1 - List all products
        2 - Show total product quantity
        3 - Make an order
        4 - Quit the program
        Handles invalid inputs gracefully."""
    while True:
        try:
            print(  "1. List all products in store\n"
                    "2. Show total amount in store\n"
                    "3. Make an order\n"
                    "4. Quit"
            )
            while True:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    show_products()
                elif choice == 2:
                    show_quantities()
                elif choice == 3:
                    make_order()
                elif choice == 4:
                    return
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4")


def main():
    """Entry point for the program. Launches the main menu."""
    menu()


if __name__ == "__main__":
    main()