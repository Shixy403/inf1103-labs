# ==============================================================================
# INF1103 Lab 6: Classes
# File: inventory_manager.py
# ==============================================================================
class Product:
    """Class representing an individual product with encapsulated attributes."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = str(product_id).strip()
        self.__name = str(name).strip()
        self.__price = float(price)
        self.__stock = int(stock)

    def get_id(self):
        """Return the product ID."""
        return self.__product_id

    def get_name(self):
        """Return the product name."""
        return self.__name

    def get_price(self):
        """Return the product price."""
        return self.__price

    def get_stock(self):
        """Return the current stock."""
        return self.__stock

    def update_stock(self, quantity: int):
        """Update stock quantity safely within the object."""
        self.__stock = quantity

    def display_information(self):
        """Display details of this product."""
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(self):
        """Convert product attributes to a dictionary for JSON serialization."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }