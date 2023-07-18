# Challenge: Print the Max Sum of Values
# Write a Python program that prints the maximum sum of the values in a dictionary.
# my_dict = {
# 	"a": [1, 2, 3],
# 	"b": [4, 0, -4],
# 	"c": [3, 5, 9],
# 	"d": [45, 12, 100]
# }
# This should be the output:
# 157 - d
my_dict = {
	"a": [1, 2, 300],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
};
temp = 0;
for i in my_dict.items():
    if temp < sum(i[1]):
        key = i[0];
        temp = sum(i[1]);
print(f'Max Sum at {key} and the value is {temp}');
