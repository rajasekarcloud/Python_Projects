# Challenge: Check if a Year is a Leap Year or Not (*)
# This is how you can determine if a year is a leap year or not:
# if (year is not divisible by 4) then (it is a common year).
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)
year: int = int(input("Enter a year: "));
if year%4 != 0 or year%100 !=0 or year%400 !=0:
    print(f'Common Year {year}');
else:
    print(f'Leap Year {year}');
