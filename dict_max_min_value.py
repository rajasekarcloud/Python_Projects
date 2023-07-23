# Challenge: Find the Maximum Value in a Dictionary
# Write a Python program that prints the largest value in a dictionary.
# If the dictionary is empty, print None.
data = {'a':5,'b':4,'c':9,'d':13};
temp = 1;
for i in data.values():
    if i > temp:
        temp = i;
print(f'Maximum value in the dict is {temp}');
# Another Method
if data:
    max_value = max(set(data.values()));
    min_value = min(set(data.values()));
    print(max_value, min_value);
else:
    print(f'Empty Dict');

