from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]


def make_object():
    best_buy = Store(product_list)
    return best_buy


def products_list():
    products = make_object().get_all_products() #list
    return products


def show_products():
    for index, product in enumerate(products_list()):
        print(f"{index + 1}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


def show_quantities():
    total_quantity = 0
    for quantity in products_list():
        total_quantity += quantity.quantity
    print(f"Total of {total_quantity} in Store")


def make_order():
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
                    break
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4")


def main():
    menu()


if __name__ == "__main__":
    main()