# Challenge: Count Characters in a File
# Write a Python program that counts the number of characters in a file.
# Count all the characters in the file, including commas and quotes.
# Do not count spaces and remove \n (new line) characters.
file_name="count.txt";
count=0;
with open(file_name) as file:
    for i in file.readlines():
        count += (len(i.rstrip("\n".replace(" ",""))));
    print(f'Total Characters: {count}');
