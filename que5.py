from que5_config.triangle import Triangle
from que5_config.circle import Circle
from que5_config.rectangle import Rectangle


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