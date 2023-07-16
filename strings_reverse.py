# Challenge: Reverse a String
# Write a Python Program that prints the reversed version of a string.
# The program must preserve uppercase and lowercase letters.
# If the string is empty, print it intact.
# Method: 1
data: str = str(input("Enter A String: "));
print(''.join(reversed(data)));
# Method: 2
print(data[::-1]);
# Method: 3
for i in range(len(data)-1,-1,-1):
    print(data[i],end='');
print("\n");
