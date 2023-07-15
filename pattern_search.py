# Challenge: Check a Pattern using a Regular Expression (*)
# Write a Python program that checks if a string start with the string "My" and ends with the string "blue".
# $ match end of a string
# ^ match start of a string
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html
import re;
data: str = input("Enter a string: ");
regex = "^My[\w\s]+blue$";
#\w = letters ( Match alphanumeric character, including “_”)
#\s = space
if re.search(regex,data):
    print("Match");
else:
    print("Not Match");
