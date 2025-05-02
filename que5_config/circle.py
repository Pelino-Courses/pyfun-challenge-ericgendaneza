from .shape import Shape
class Circle(Shape):
    """
    Class representing a circle.
    Inherits from the Shape class and implements specific behaviors for circles.
    """

    def __init__(self, radius, color="white"):
        """
        Constructs all the necessary attributes for the circle object.

        Parameters:
        ----------
            radius : float
                The radius of the circle.
            color : str
                The color of the circle. Default is "white".

        Raises:
        ------
            ValueError: If the radius is negative.
        """
        super().__init__(color)
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius


    def area(self):
        """
        Calculates the area of the circle.

        Returns:
        -------
            float: The area of the circle.
        """
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
        -------
            float: The perimeter of the circle.
        """
        return 2 * 3.14159 * self.radius

    def __str__(self):
        """
        Returns a string representation of the circle.

        Returns:
        -------
            str: A string representation of the circle.
        """
        return f"Circle(radius={self.radius}, color={self.color})"
