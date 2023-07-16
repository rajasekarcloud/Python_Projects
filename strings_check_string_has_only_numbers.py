# Challenge: Check if a String Only Contains Numbers
data: str = input("Enter a string: ");
if data.isdigit():
    print(f'{data} contains only digits');
else:
    print(f'{data} contains Alphabet & Numerical');

# Method:2
num = [];
for i in range(10):
    num.append(str(i)); # Reason for adding str we are going take numbers as strings for easy comparisont to check in the list
count=0;
for i in data:
    if i in num:
        count +=1;

if count == len(data)-1:
    print(f'{data} contains only digits');
else:
    print(f'{data} contains alpha numbers');

