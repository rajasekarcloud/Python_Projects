# Challenge: Remove Characters at Even Indices
# Write a Python program that prints the string s without the characters located at even indices.
# If the string is empty or only has one character, print it without any changes.
data: str = str(input("Enter a string: "));
if len(data) <=1:
        print(f'{data}');
else:
    for i in range(len(data) - 1):
        if i%2 != 0:
            print(data[i],end=' ');
