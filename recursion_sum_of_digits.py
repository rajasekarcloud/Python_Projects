# Challenge: Find the Sum of the Digits of a Positive Integer
# Write a Python program that calculates and prints the sum of the digits of a positive integer num.
# 23 -> 5
# 111 -> 3
# 1234 -> 10
def sum_of_digit(num):
    if num == 1:
        return 1;
    else:
        return (num%10) + sum_of_digit(num // 10);
print(sum_of_digit(1234));
