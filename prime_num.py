# Challenge: Check if a Number is Prime
# Write a Python program that checks if a number is prime or not.
# If the number is prime, it should print "Prime".
# If the number is not prime, it should print "Not prime".
# A prime number is only divisible by 1 and by itself. It is not the product of two smaller natural numbers.
num: int = int(input("Enter a number: "));
if num == 1 or num == 2 or num == 3:
    print(f'{num} is PRIME');
elif num == 0:
    print(f'{num} is ZERO');
else:
    for i in range(2,num):
        if num % i == 0:
            print(f'{num} is NOT PRIME');
            break;
        else:
            print(f'{num} is PRIME');
            break;
