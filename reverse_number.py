#Challenge: Print Digits in Reverse Order
# Input= 321 and output = 123
num=321;
while num > 1:
    mod = num % 10;
    div = round(num / 10);
    print(mod,end="");
    num = div;
