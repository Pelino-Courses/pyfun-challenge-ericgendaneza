class Shape:
    """
    Base class for all geometric shapes.
    This class provides common attributes and methods for all shapes
    and serves as a base for specific shape classes.
    """

    def __init__(self, color="white"):
        """
        Constructs all the necessary attributes for the shape object.

        Parameters:
        ----------
            color : str
                The color of the shape. Default is "white".
        """
        self.color = color

    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        """
        Returns a string representation of the shape.
        This method should be overridden by subclasses.
        """
        return f"Shape(color={self.color})"