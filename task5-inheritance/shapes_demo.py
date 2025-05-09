from shapes import Triangle
from shapes import Circle
from shapes import Rectangle

try:

    circle = Circle(5, "red")
    rectangle = Rectangle(4, 6, "blue")
    triangle = Triangle(3, 4, "green")

    print(circle)
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")

    print(rectangle)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

    print(triangle)
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")

except Exception as err:
    print("Unexpected Error:",err)