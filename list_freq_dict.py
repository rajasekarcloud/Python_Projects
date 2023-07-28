# Challenge: Make a Frequency Dictionary from the Elements of a List (*)
# Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).
# ["a","a","b","c","a","b"] -> {'a':3,'b':2,'c':1}
list = ["a","a","b","c","a","b"];
ans = {};
for i in list:
    if i not in ans:
        ans[i] = 1;
    else:
        ans[i] +=1;
print(ans);
