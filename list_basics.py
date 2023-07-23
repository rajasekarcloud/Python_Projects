# Challenge: Multiply all Elements in a List
# Write a Python program that multiplies all the items in a list by the value of the variable factor.
# Input - [2,3,4,5] , Factor - 3 , Output = [6,9,12,15];
num = [2,3,4,5];
factor = 3;
result = [];
for i in num:
    result.append(i * factor);
print(result);

# Another Method using enumerate - This can update the num list dyamically instead using another list
for index,value in enumerate(num):
    num[index] = value * factor;
print(num);

# Challenge: Print Elements on the Same Line Without Commas
# Input: [3,4,5,6] -> 3,4,5,6
data = [3,4,5,6];
print(*data); #* list can convert list to a string.

# Challenge: Get Max and Min Values
data = [3,4,5,6];
print(min(data),max(data));

# Another Method using loop
data = [3,4,5,6];
temp = 1;
for i in data:
    if i > temp:
        temp = i;
print(f'Max {temp}');

# Challenge: Check if List is Empty or Not
data = [];
if data:
    print(f'"Not Empty');
else:
    print(f'Empty');

# Challenge: Print the Elements and Their Indices
data = "Hello World";
for key,value in enumerate(data):
    print(f'{key} -> {value}');
# Another Method
for i in range(len(data) - 1):
    print(i,"->", data[i]);

# Challenge: Remove Matching Element
# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
# Input - [1,2,3,4], Element to remove - 2 and output [1,3,4]
data = [1,2,3,4];
remove_value = 2;
print(data.index(remove_value)); # Return index of value 2
print(data.pop(data.index(remove_value)));
print(data);

# Challenge: Remove Duplicates from a List
data = [1,2,3,4,2];
print(set(data));

# Another Method:
data = [1,2,3,4,2];
dup_list = [];
for i in data:
    if i not in dup_list:
        dup_list.append(i);
print(dup_list);

# Challenge: Count Elements Greater than 3
# Write a Python program that counts the number of elements in a list with value greater than 3
data = [1,2,3,4,5];
count = 0;
for i in data:
    if i > 3:
        count +=1;
print(f'Elements Greater Than 3: {count}');

# Challenge: Find the Intersection of Two Sets
set1 = {1,2,3,4};
set2 = {4,5,6};
intersec = set();
for i in set1:
    if i in set2:
        intersec.add(i);
print(f'Intersection of set1 and set2 : {intersec}');

# Another Method

print(set1.intersection(set2));
