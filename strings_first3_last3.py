# Challenge: First and Last Three Characters of a String
# Write a Python program that prints the first and last three characters of the string s as a single string.
# If the string has less than six characters, print an empty string (blank output).
data: str = str(input("Enter a string: "));
if len(data) < 6:
    print ("String is less than 6 characters");
else:
    print(f'First 3 Characters: {data[:3]}');
    print(f'Last 3 Characters: {data[len(data)-3:]}');
