#Challenge: Balanced Square Brackets
#Description:
#Write a Python program that determines if a string with square brackets is balanced (if it has opening and closing square brackets in the correct order).
#You can write this implementation as a function.
#Return the value True if the string is balanced and False if it is not balanced.
#You may assume that the string only contains square brackets [ and ].
# "[ ]" - True
# "][" - False
# "[] []" - True
# "][]" - False

def bracket_validator(data):
   # We are going to add +1 for [ and -1 for ]
    count = 0;
    for i in data:
        if i == '[':
            count +=1;
            print("[ ",count);
        elif i == ']':
            count -=1;
            print("] ",count);
        if count < 0: # If count is a negative number then its unbalanced bracket
            return False;
        else:
            return True;

data: str = input("Enter a string in brackets: ");
print(bracket_validator(data));
