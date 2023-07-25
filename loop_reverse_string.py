# Challenge: Reverse a String using a Loop
data="Hello";
print(data[::-1]); # Reverse
for i in range(len(data)-1,-1,-1): # We are reversing the loop from 4,3,2,1,0 
    print(data[i],end="");
