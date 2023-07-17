# Challenge: Make a Dictionary from Nested Lists
# Write a Python program that creates a dictionary from the values contained in nested lists.
# Each nested list has this format [value1, value2].
# value1 should be the key in the dictionary and value2 should be its corresponding value.
# If there are no nested lists, print an empty dictionary.
# If this is the list that contains nested lists:
# {[["a", 1], ["b", 2], ["c", 3], ["d", 4]]}
# Result {"a": 1, "b": 2, "c": 3, "d": 4}
data = [["a", 1], ["b", 2], ["c", 3], ["d", 4]];
result = {};
for i in data:
    result[i[0]] = i[1];
print(result);
