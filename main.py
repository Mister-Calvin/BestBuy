from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()  #list


def show_products():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


def show_quantities():
    total_quantity = 0
    for quantity in products:
        total_quantity += quantity.quantity
    print(total_quantity)


def make_order():

    order = []
    which_product = int(input("Which product do you want to buy: "))
    which_quantity = int(input("Which quantity do you want to buy: "))
    selected_product = products[which_product-1]
    order.append((selected_product, which_quantity))
    print(f"Total: {best_buy.order(order)}")


def menu():
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


def main():
    menu()


if __name__ == "__main__":
    main()