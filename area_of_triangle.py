# Challenge: Compute the Area of a Triangle
# Write a Python program that computes the area of a triangle from its base and height.
# The program should print the area of the triangle rounded to two decimal places (if necessary).
# The values of base and height should be entered by the user.
# The area of a triangle is found with this formula: (base*height)/2
base:int = int(input("Enter Base: "));
height: int = int(input("Enter Height: "));
print(f'Area of triangle {(base * height)/2}');
