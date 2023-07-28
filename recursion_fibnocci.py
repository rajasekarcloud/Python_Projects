# Challenge: Find the nth Fibonacci Number
# The value of n represents the position of the element in the sequence.
# The initial value of n should be 0.
# You may assume that the value of n is a non-negative integer.
def fib(num):
    if num == 0:
        return 0;
    elif num == 1:
        return 1;
    else:
        return fib(num - 1) + fib(num - 2);
num = 5;
print(fib(num));
