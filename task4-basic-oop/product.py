class Product:
    """
    A class to represent a product in an inventory system.

    Attributes:
    ----------
    name : str
        The name of the product.
    price : float
        The price of the product.
    quantity : int
        The quantity of the product in stock.

    Methods:
    -------
    add_inventory(amount):
        Adds a specified amount to the product's quantity.
    
    remove_inventory(amount):
        Removes a specified amount from the product's quantity.
    
    total_value():
        Calculates the total value of the product (price × quantity).
    
    display_info():
        Displays the product's information.
    """

    def __init__(self, name, price, quantity):
        """
        Constructs all the necessary attributes for the product object.

        Parameters:
        ----------
            name : str
                The name of the product.
            price : float
                The price of the product.
            quantity : int
                The quantity of the product in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
    def add_inventory(self, amount):
        """
        Adds a specified amount to the product's quantity.

        Parameters:
        ----------
            amount : int
                The amount to add to the product's quantity.
        
        Raises:
        ------
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self.quantity += amount


    def remove_inventory(self, amount):
        """
        Removes a specified amount from the product's quantity.

        Parameters:
        ----------
            amount : int
                The amount to remove from the product's quantity.
        
        Raises:
        ------
            ValueError: If the amount is negative or greater than current quantity.
        """
        if amount < 0:
            raise ValueError("Amount to remove cannot be negative.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than current quantity.")
        self.quantity -= amount

        
    def total_value(self):
        """
        Calculates the total value of the product (price × quantity).

        Returns:
        -------
            float: The total value of the product.
        """
        return self.price * self.quantity


    def display_info(self):
        """
        Displays the product's information.

        Returns:
        -------
            str: A string representation of the product's information.
        """
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total Value: {self.total_value()}"