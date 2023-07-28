# Challenge: Flatten a List that Contains Lists (*)
# Write a Python program that prints a "flattened" version of a list that contains nested lists.
# "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.
# [[1,2,3],[4,5,6],[7,8,9]] = [1,2,3,4,5,6,7,8,9]
list1=[[1,2,3],[4,5,6],[7,8,9]];
flat=[];
for i in list1:
    if isinstance(i, list): # This will return if i is a valid list datatype.
        for x in i:
            flat.append(x);
print(flat);
