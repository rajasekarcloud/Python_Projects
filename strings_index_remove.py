# Challenge: Remove nth Character from a String
# Write a Python program that prints the string s without the character at index n.
# If the index n is out of range, print the string s intact.
# If the string s is empty, print the string s intact.
# Input: Hello -> index = 1 -> Output -> Hllo
data:str = input("Enter a string: ");
index:int = int(input("Enter an index: "));
if index > len(data):
    print(f'Entered index is out of range. String length {len(data)}');
else:
    for i in range(len(data)-1):
        if i != index:
            print(data[i],end=' ');

