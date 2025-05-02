from .shape import Shape

class Rectangle(Shape):

    """
    Class representing a rectangle.
    Inherits from the Shape class and implements specific behaviors for rectangles.
    """

    def __init__(self, width, height, color="white"):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters:
        ----------
            width : float
                The width of the rectangle.
            height : float
                The height of the rectangle.
            color : str
                The color of the rectangle. Default is "white".

        Raises:
        ------
            ValueError: If the width or height is negative.
        """
        super().__init__(color)
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        -------
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        -------
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        -------
            str: A string representation of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"
