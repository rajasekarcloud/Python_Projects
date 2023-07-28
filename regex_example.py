# Challenge: Check a Pattern using a Regular Expression (*)
# Write a Python program that checks if a string start with the string "My" and ends with the string "blue".
# My favorite color is blue = Match
# My shoes are blue = Match
# My favorite color is red = No Match
# Hello I am 12 years old = No Match
import re;
word: str = str(input("Enter a word: "))
regex = "My[\w\s]+blue$";
if re.search(regex,word):
    print(f'Match');
else:
    print(f'No Match');
