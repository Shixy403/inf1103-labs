# ==============================================================================
# INF1103 Lab 6: Classes
# File: inventory_manager.py
# ==============================================================================
import json
import os



class Product:
    """Class representing an individual product with encapsulated attributes."""

    def __init__(self, product_id: str, name: str, price: float, stock: int): # product_id, name, price, stock as parameters
        # .__ sets the attributes as PRIVATE, preventing direct access from outside the class
        self.__product_id = str(product_id).strip()
        self.__name = str(name).strip()
        self.__price = float(price)
        self.__stock = int(stock)

    def get_id(self):
        return self.__product_id # getter for product ID

    def get_name(self):
        return self.__name  # getter for product name

    def get_price(self):
        return self.__price # getter for product price

    def get_stock(self):
        return self.__stock # getter for product stock

    def update_stock(self, quantity: int):
        self.__stock = quantity # setter for product stock

    def display_information(self):
        # prints product information
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(self):
        # Convert product attributes to a dictionary repreentation for JSON
        return {
            "id": self.__product_id,    # store product_id under the key "id"
            "name": self.__name,        # store name under the key "name"
            "price": self.__price,      # store price under the key "price"
            "stock": self.__stock       # store stock under the key "stock"
        }

class Inventory:
    def __init__(self):
        # initialize an empty list to hold multiple Product objects
        self.products = []

    def add_product(self, product: Product):
        # append a new Product instance into our inventory list
        self.products.append(product)

    def search_product(self, product_id: str):
        # loop through all Product objects in our list to find an ID match
        for product in self.products:
            if product.get_id() == product_id:
                return product # return the matched Product object
        return None # return None if no product matches the ID

    def display_all(self):
        # print header banner
        print("\nCurrent Inventory")
        print("-" * 48)

        # delegate printing to each individual product object
        for product in self.products:
            product.display_information()

        print("-" * 48)

    def get_all(self):
        # return the full list of Product objects (used when saving to JSON)
        return self.products


# Persistence Functions (JSON File Handling), not used in class for Single Responsibility Principle
def save_inventory(filename, inventory: Inventory):
    # build a list of dictionaries by calling .to_dict() on each Product object
    data = [product.to_dict() for product in inventory.get_all()]

    # write the list of product dictionaries into the JSON file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory(filename, inventory: Inventory):
    # check if the JSON file exists on disk
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            # recreate Product objects from loaded dictionaries and add to inventory
            for item in data:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                inventory.add_product(product)

            print(f"{filename} found.")
            print("Inventory loaded successfully.")
            return

        except (json.JSONDecodeError, OSError):
            print("Unable to load inventory. Starting with empty inventory.")
            return

    # if file does not exist, start fresh
    print(f"{filename} not found. Starting with empty inventory.")



def add_product(inventory: Inventory):
    # prompt user for product details
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity.")
        return

    # create a new instance of Product and add it to the Inventory collection
    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory: Inventory):
    # prompt user for product ID to find the target object
    product_id = input("Enter Product ID: ").strip()

    # retrieve Product object from Inventory
    product = inventory.search_product(product_id)

    if product:
        print("\nProduct Found:")
        print("Name:", product.get_name())
        print("Current Stock:", product.get_stock())

        try:
            new_stock = int(input("New Stock Quantity: "))
        except ValueError:
            print("Invalid stock quantity.")
            return

        # call update_stock method on the Product object to change its private state
        product.update_stock(new_stock)
        print("Stock updated successfully!")
        return

    print("Product not found.")


def search_product(inventory: Inventory):
    # prompt user for product ID to search
    product_id = input("Enter Product ID: ").strip()

    # query the inventory collection
    product = inventory.search_product(product_id)

    if product:
        print("\nProduct Found")
        print("-" * 48)
        print("ID:", product.get_id())
        print("Name:", product.get_name())
        print(f"Price: ${product.get_price():.2f}")
        print("Stock:", product.get_stock())
        print("-" * 48)
        return

    print("Product not found.")


def display_all(inventory: Inventory):
    # delegate the display operation directly to the Inventory class
    inventory.display_all()



def main():
    filename = "inventory.json"

    # instantiate the Inventory container object
    inventory = Inventory()

    # load saved products into the inventory object on startup
    load_inventory(filename, inventory)

    while True:
        # print main options menu
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(filename, inventory)

        elif choice == "6":
            # auto-save inventory to disk on exit
            save_inventory(filename, inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()