# Challenge: Print the Character at a Specific Index
# Write a Python program that prints the character at index i in the string s.
# User enters the index and prints the character
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"
data: str = str(input("Enter a string: "));
if data:
    index: int = int(input("Enter a index: "));
    if index > len(data) - 1:
        print(f'{index} is out of range.');
    else:
        print(f'{index} -> {data[index]}');
else:
    print(f'Empty String');
