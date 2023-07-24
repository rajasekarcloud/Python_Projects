# Challenge: Print a Pattern using Loops
# Write a Python program that prints a triangular pattern like the ones shown below in the examples.
# If the value of n is 3:
#
# *
# * *
# * * *
def triangle(count):
    for row in range(count):
        for column in range(row + 1):
            print("*", end=" ");
        print("\n");
triangle(3);
