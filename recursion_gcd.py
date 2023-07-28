# Challenge: Find the Greatest Common Divisor
# Write a Python program that finds and prints the Greatest Common Divisor (GCD) of the numbers a and b (the largest number that divides them both).
#  For example, the GCD of 8 and 12 is 4, that is,
# gcd(8,12) is 4.
def gcd(a,b):
    if b==0:
        return a;
    else:
        return gcd(b,a % b);

print(gcd(8,12));
