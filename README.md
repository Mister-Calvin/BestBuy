# BestBuy

BestBuy is an object-oriented Python command-line application that models a small retail store. It manages products, inventory, and multi-item orders while keeping the business logic separate from the user interface.

## Features

- List all active products with prices and available quantities
- Calculate the total number of items in stock
- Build an order containing multiple products
- Calculate the total order value
- Update inventory after each purchase
- Deactivate products automatically when their stock reaches zero
- Validate product data and requested quantities

## Project structure

- `products.py` defines the `Product` class and its inventory rules.
- `store.py` defines the `Store` class and handles products and orders.
- `main.py` provides the interactive command-line menu.

## Run locally

The application requires Python 3 and has no third-party dependencies.

```bash
git clone https://github.com/Mister-Calvin/BestBuy.git
cd BestBuy
python3 main.py
```

The menu allows you to list products, inspect the total inventory, create an order, or exit the application.

## OOP concepts demonstrated

- Encapsulation of product and store behavior
- Composition of a store from multiple product objects
- Validation of object state and purchase quantities
- Inventory state management through class methods
