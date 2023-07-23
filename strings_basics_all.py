# Challenge: Change Commas by Dots
# Write a Python program that prints a version of the string s with all commas replaced by dots.
# Hello, World -> Hello. World
data="Hello, World";
print(data.replace(',','.'));

# Challenge: Check if String Contains All Letters in the Alphabet
# If the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").
# If it does, print True. Else, print False.
# Before comparing the characters, you should convert the string to lowercase.
# Hello -> False
# hello -> True
data = "helloworld";
data = data.lower();
print(data.isalpha()); #If the string has space then it returns False

# Challenge: Remove Spaces from a String
# If the string doesn't contain spaces, print it intact.
# Input: "Hello, World"; -> "Hello,World"
data="Hello, World";
print(data.replace(" ",""));

# Challenge: Check if a String Starts with a Prefix
# data="Hello" and input="He" -> True
# data="Nora" and input="Circum" -> False
# For example, "A" should not be equivalent to "a".
data="Hello";
prefix: str = str(input("Enter Prefix: "))
print(data.startswith(prefix));

# Another Method
print(data[:len(prefix)] == prefix);

# Challenge: Check if a String Ends with a Suffix
data="Hello";
suffix: str = str(input("Enter Suffix: "));
print(data.endswith(suffix));

# Another Method
print(data[-len(suffix):] == suffix);

# Challenge: Sort Words in Alphabetical Order (*)
# Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.
# Hello World -> ehllo dlorw
data = "Hello World";
new="";
print(data.split(" ")); # Splits data in list
for i in data.split(" "):
    lower_data = i.lower();
    sorted_data = "".join(sorted(lower_data));
    new += sorted_data + " ";
print(new);

# Challenge: Count Repeated Characters (*)
# Write a Python program to count the number of repeated characters in the string s.
# Hello -> 1 character "l" repeated.
data = 'Hellooo';
rep_char = [];
rep = {};
for i in data:
    if data.count(i) > 1 and i not in rep_char:
        rep_char.append(i);
print(rep_char); # This will print only the repeated characters
for i in rep_char:
    rep[i] = data.count(i);
print(rep);

