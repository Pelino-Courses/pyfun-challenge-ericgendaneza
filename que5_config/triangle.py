from .shape import Shape

class Triangle(Shape):
    """
    Class representing a triangle.
    Inherits from the Shape class and implements specific behaviors for triangles.
    """

    def __init__(self, base, height, color="white"):
        """
        Constructs all the necessary attributes for the triangle object.

        Parameters:
        ----------
            base : float
                The base of the triangle.
            height : float
                The height of the triangle.
            color : str
                The color of the triangle. Default is "white".

        Raises:
        ------
            ValueError: If the base or height is negative.
        """
        super().__init__(color)
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        self.base = base
        self.height = height

    def area(self):
        """
        Calculates the area of the triangle.

        Returns:
        -------
            float: The area of the triangle.
        """
        return 0.5 * self.base * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the triangle.
        Note: This is a placeholder method. Actual implementation would require
        knowledge of all three sides of the triangle.

        Returns:
        -------
            float: The perimeter of the triangle.
        """
        raise NotImplementedError("Perimeter calculation requires all three sides.")


    def __str__(self):
        """
        Returns a string representation of the triangle.

        Returns:
        -------
            str: A string representation of the triangle.
        """
        return f"Triangle(base={self.base}, height={self.height}, color={self.color})"
