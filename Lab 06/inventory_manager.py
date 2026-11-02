# ==============================================================================
# INF1103 Lab 6: Classes
# File: inventory_manager.py
# ==============================================================================


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

    def set_stock(self, quantity: int):
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
    