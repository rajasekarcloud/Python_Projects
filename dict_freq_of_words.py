# Challenge: Make a Frequency Dictionary for the Characters in a String (*)
# Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).
# Input: "Hello, World"
# {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
data="Hello, World";
freq = {};
for i in data:
    if i.isalnum():
        if i in freq:
            freq[i] +=1;
        else:
            freq[i] = 1;
print(freq);
