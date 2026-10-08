# ==============================================================================
# INF1103 Lab 5: Data Manipulation
# File: inventory_manager.py
# ==============================================================================
import json
import os


def load_inventory(filename):
    """Load inventory from a JSON file."""

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                inventory = json.load(file)

            print(f"{filename} found.")
            print("Inventory loaded successfully.")

            return inventory

        except (json.JSONDecodeError, OSError):
            print("Unable to load inventory. Starting with empty inventory.")
            return []

    print(f"{filename} not found. Starting with empty inventory.")
    return []


def add_product(inventory):
    """Add a new product to the inventory."""

    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity.")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    print("Product added successfully!")


def update_stock(inventory):
    """Update the stock quantity of an existing product."""

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid stock quantity.")
                return

            product["stock"] = new_stock
            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    """Search for a product by product ID."""

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("-" * 48)
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("-" * 48)
            return

    print("Product not found.")


def display_all(inventory):
    """Display all products in the inventory."""

    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)


def main():

    filename = "inventory.json"

    inventory = load_inventory(filename)

    display_all(inventory)


if __name__ == "__main__":
    main()