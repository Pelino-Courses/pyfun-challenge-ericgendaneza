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
