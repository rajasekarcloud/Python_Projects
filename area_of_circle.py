# Challenge: Calculate the Area of a Circle
# Write a Python program that finds the area of a circle from the value of the diameter d.
# The value of d should be provided by the user.
# The area of a circle is equal to pi*(radius)^2. The radius is the value of the diameter divided by 2.
# Round the value of the area to two decimal places.
# Eg: Input 10 = 78.54
# 3.14(10/2)^2  = 3.14X(5)^2 = 3.14 * 25 = 78.5
dia: int = int(input("Enter the diameter: "));
rad: float = float(dia/2);
# Value of pi = 3.14;
area = 3.14*(rad)**2;
print(f'Area of a circle {area}');
