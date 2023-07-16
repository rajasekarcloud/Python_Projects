# Challenge: Replace a Character in a String
# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
# curr_char and new_char are variables that contain strings with a single character.
# You may assume that new_char will not be an empty string.
# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
# If input is "Hello" and curr_char 'l' and new_char 's' -> Output -> "Hesso"
data: str = input("Enter A String: ");
curr_char: str = input("Enter a current character: ");
new_char: str = input("Enter a new character: ");
data = data.replace(curr_char,new_char);
print(f'Replaced Letter: {data}');
