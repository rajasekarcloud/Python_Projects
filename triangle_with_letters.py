# Challenge: Triangular Letters Pattern (*)
# If the value of n is 3, this is the expected output:
#
# A
# B B
# C C C
import string;
number_of_row = 3;
temp=0; # To initialze the starting character as "A"
# print(string.ascii_uppercase[0:3]); # Prints ABC
for row in range(number_of_row):
    for column in range(row + 1):
        print(string.ascii_uppercase[temp],end=" ");
    temp +=1;
    print("\n");
