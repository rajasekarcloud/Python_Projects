# Guess the number range between 1 and 10
from random import randint;
while True:
    try:
        in_number = int(input("Enter a number: "));
        if in_number > 10:
            print("Enter number between 1 and 10");
            continue;
        sys_number = randint(1,10);
        if in_number == sys_number:
            print(f"You guessed a the right number {in_number}");
        else:
            print(f"You are wrong. Its {sys_number}");
    except ValueError as e:
        print("Enter a valid number");
        continue;
