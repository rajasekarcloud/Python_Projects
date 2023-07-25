# Challenge: Floyd's Triangle (*)
# If n is equal to 3:
#
# 1
# 2 3
# 4 5 6
num_of_rows=5;
temp=0;
for row in range(num_of_rows):
    for column in range(row + 1):
        temp+=1;
        print(temp,end=" ");
    print("\n");
