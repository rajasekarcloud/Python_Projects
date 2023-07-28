# Challenge: Solve a Power Recursively
# Write a Python program that find the value of a raised to the power b recursively.
# The operation is a**b in Python, where a is the base and b is the exponent.
# 2 and 3 -> 2^3 = 8
def calculate_power(a,b):
    if b == 1:
        return a;
    else:
        return a * calculate_power(a, b-1);
print(calculate_power(2,3));
