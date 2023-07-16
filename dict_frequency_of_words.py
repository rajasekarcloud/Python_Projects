# Challenge: Find Frequency of Values in a Dictionary
# The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).
# If the dictionary is empty, print an empty dictionary.
my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 };
# Expected Output:

# freq_dict = {
# 	4: 3
# 	2: 2
# 	7: 3
# }

freq_dict = {};

for i in my_dict.values():
    if i in freq_dict:
        freq_dict[i] +=1;
    else:
        freq_dict[i] = 1;
print(my_dict);
print(freq_dict);
