# Challenge: Convert Dictionary into a List of Lists (*)
# Write a Python program that takes the content of a dictionary and converts it into a list of lists.
# Each nested list should contain a key as the first element and its corresponding value as the second element.
# Print the final list of lists.
# product_info = {
# 	"description": "shoe",
# 	"price": 4.56,
# 	"colors": ["green", "blue", "red"],
# }
# Output: [['description', 'shoe'], ['price', 4.56], ['colors', ['green', 'blue', 'red']]]
product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
};

list=[];
for key,value in product_info.items():
    list.append([key,value]);

print(list);
