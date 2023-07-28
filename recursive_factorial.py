# Challenge: Recursive Factorial
# The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1, the product of all positive integers less than or equal to the number.
# The value of 0! is equal to 1 by mathematical convention.
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(num):
    if num == 1:
        return 1;
    else:
        return num * factorial(num - 1);
print(factorial(5));
