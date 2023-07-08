# Dice game
# The -> int at the end of the function definition indicates that the function returns an integer.
# This is known as type hinting and is used to help with code readability and debugging.
# User get an option how many times dice to roll
# And display that many values between 1 and 10
# Eg: input 3 and output as 3,4,6
# Output is a list
from random import randint;
def dice(in_number) -> list[int]: # -> Type hinting to state what datatype the function returns.
    rolls: list[int] = [];
    for i in range(in_number):
        rolls.append(randint(1,10));
    return rolls;

in_number = int(input("How many time to roll dice? "));
if in_number > 0 and in_number < 10:
    print(dice(in_number));
else:
    print("Enter number greater than 0 and less than 10");
