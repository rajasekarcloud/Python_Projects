# Challenge: Sort Lists in Ascending Order (*)
# my_dict = {
# 	"a": [4, 3, 2],
# 	"b": [5, 3, 7],
# 	"c": [1, 9, 10],
# 	"d": [3, 4, 1]
# }
# Output: my_dict = {
# 	"a": [2, 3, 4],
# 	"b": [3, 5, 7],
# 	"c": [1, 9, 10],
# 	"d": [1, 3, 4]
# }

my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
};
for i in my_dict.keys():
    my_dict[i] = sorted(my_dict.get(i));
    
print(my_dict);
