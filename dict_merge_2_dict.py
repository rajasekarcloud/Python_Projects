# Challenge: Merge Two Dictionaries
# Write a Python program that merges two dictionaries and prints the resulting dictionary.
# my_dict1 = {"a": 1, "b": 2, "c": 3}
# my_dict2 = {"c": 4, "d": 6, "e": 8}
# final_dict = {'a': 1, 'b': 2, 'c': 4, 'd': 6, 'e': 8}
my_dict1 = {"a": 1, "b": 2, "c": 3};
my_dict2 = {"c": 4, "d": 6, "e": 8,"a":10};
print(my_dict1 | my_dict2);
mydict3 = my_dict1 | my_dict2; # a=1 is overwritten by a=10
print(mydict3);
