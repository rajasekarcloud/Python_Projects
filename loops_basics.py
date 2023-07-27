# Challenge: Sum of First 100 Positive Integers
sum = 0;
for i in range(1,101):
    sum = sum + i;
print(f'Sum of first 100 {sum}');

# Challenge: Print the Multiplication Table
# The values displayed should go from n x 1 up to n x 10 with a descriptive format
num: int = int(input("Enter table: "));
for i in range(1,11):
    print(f'{num} * {i} = {num * i}');

# Challenge: Calculate Factorial
# Write a Python program that calculates the factorial of a given number n.

def factorial(fact):
    if fact == 1:
        return fact;
    else:
        return fact * factorial(fact - 1);
fact: int = int(input("Enter number: "));
print(factorial(fact));

# Challenge: First 100 Even Numbers
# Write a Python program that prints the first 100 even numbers (from 2 to 200 inclusive).
count = 0;
for i in range(1,201):
    if i%2 == 0:
        print(f'{i}');
        count +=1;
    if count == 100:
        break;
