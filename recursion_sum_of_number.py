# Challenge: Find the Sum of a List using Recursion
# Write a Python program that finds the sum of a list (or tuple) of numbers recursively.
# If the list (or tuple) is empty, print 0.
# [1,2,3] = 6
# Using for loop

def sum(num):
    if len(num) == 0:
        return 0;
    else:
        count = 0;
        for i in num:
            count = count + i;
        return count;

data = [1,2,3];
print(sum(data));
