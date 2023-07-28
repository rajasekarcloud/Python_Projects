# Challenge: Print Common Elements in Two Lists
# Write a Python program that prints a list with the elements that listA and listB have in common.
listA=[1,2,3,4,5];
listB=[3,4,5,6];
for i in listA:
    if i in listB:
        print(f'Common Elements: {i}');
