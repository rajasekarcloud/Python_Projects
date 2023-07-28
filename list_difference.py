# Challenge: Difference Between Two Lists
# Write a Python program that prints (as a list) the elements of listA that are not in listB.
listA=[1,2,3,4];
listB=[3,4,5,6];
for i in listA:
    if i not in listB:
        print(f'{i}');
