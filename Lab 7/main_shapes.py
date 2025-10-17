from shapes.circle import area as circle_area, circumference as circle_circumference
from shapes.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from shapes.triangle import area as triangle_area, perimeter as triangle_perimeter


shape_str = input("Choose a shape: circle, rectangle, or triangle: ")

if shape_str == "circle":
    radius_str = input("Please enter the radius of the circle: ")
    radius = float(radius_str)
    print("The radius is: ", circle_area(radius), 
          "The circumference is: ", circle_circumference(radius))

if shape_str == "rectangle":
    length_str = input("Please enter the length of the rectangle: ")
    width_str = input("Please enter the width of the rectangle: ")
    length = float(length_str)
    width = float(width_str)
    print("The area of the rectangle is: ", rectangle_area(length, width),
          "\nThe perimeter of the rectangle is: ", rectangle_perimeter(length, width))


if shape_str == "triangle":
    base_str = input("Please enter the base of the triangle: ")
    height_str =input("Please enter the height of the triangle: ")
    side1_str = input("Please enter the length of the first side of the triangle: ")
    side2_str = input("Please enter the length of the second side of the triangle: ")
    side3_str = input("Please enter the length of the third side of the triangle: ")
    base = float(base_str)
    height = float(height_str)
    side1 = float(side1_str)
    side2 = float(side2_str)
    side3 = float(side3_str)
    print("The area of the triangle is: ", triangle_area(base, height),
          "\nThe perimeter of the triangle is: ", triangle_perimeter(side1, side2, side3))