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

def main():
    while True:
       try:
           in_number = input("Enter # of times to roll the dice: ");
           if in_number.lower() == 'exit':
               print("Thanks for playing");
               break;
           elif int(in_number) > 0 and int(in_number) <=10:
               # print(dice(int(in_number)));# Output comes as list [1, 2, 3, 4, 5]
            # We can unpack them
                print(*dice(int(in_number)),sep=',');
           else:
               print("Enter a number between 1 and 10")
       except ValueError as e:
           print("Enter a valid number");


if __name__ == '__main__':
    main();
