#Challenge: Read a Text File
#Write a Python program that reads a text file and saves its content line by line to a list called file_content.
file_path="basic_file.txt";
with open(file_path,"r") as file:
    for line in file:
        print(line);

# Challenge: Print the First n Lines of a File
# Write a Python program that reads a text file and prints the first n lines of the file.
# The value of n should be entered by the user.
# If the value of n is greater than the total number of lines in the file, print
# "Please enter a value for n. The file has <num_lines> lines".

file_path="basic_file.txt";
new_line: int = int(input("Enter the line number: "))
with open(file_path,"r") as file:
    line = file.readlines();
    if new_line > len(line):
        print(f'{new_line} exceeded number of lines in the file');
    else:
        for i in range(new_line):
            print(line[i].rstrip("\n")); # rstrip removes space.

# Challenge: Print the Last n Lines of a File
# Write a Python program that prints the last n lines of a text file in order.
file_path="basic_file.txt";
new_line: int = int(input("Enter the line number: "))
with open(file_path,"r") as file:
    line = file.readlines();
    if new_line > len(line):
        print(f'{new_line} exceeded number of lines in the file');
    else:
        for i in range(-new_line,0):
            print(line[i].rstrip("\n")); # rstrip removes space.
