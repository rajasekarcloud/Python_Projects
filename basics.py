# Challenge: Zero, Positive, or Negative
# Write a Python program that prints if a number num is either "Positive", "Negative", or "Zero".
data = [1,2,-1,0];
for i in data:
    if i == 0:
        print("Zero");
    elif i < 0:
        print("Negative");
    else:
        print("Positive");

# Challenge: Check Vowels and Consonants
# For example: "<char> is a <consonant | vowel>"
# "Score: 36"
# s is a consonant
# c is a consonant
# o is a vowel
# r is a consonant
# e is a vowel
# : is not a letter
#   is not a letter
# 3 is not a letter
# 6 is not a letter
vowel = ['a','e','i','o','u'];
data = "Score: 36";
for i in data:
    if i in vowel:
        print(f'{i} -> Vowel');
    elif i.isalpha():
        print(f'{i} -> Consonant');
    else:
        print(f'{i} -> Not A Letter');

# Challenge: Print Max of Three Numbers
# Write a Python program that prints the maximum of three integers (a, b, c).
a=1;
b=20;
c=3;
if (a>=b) and (a>=c):
    print(f'{a} is bigger');
elif (b>=a) and (b>=c):
    print(f'{b} is bigger');
else:
    print(f'{c} is bigger');
