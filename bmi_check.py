#Challenge: Calculate Body Mass Index
#Description:
#Write a Python program that calculates body mass index.
#The formula to calculate body mass index is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in meters squared.
#The user should be able to enter his or her height in centimeters and weight in kilograms.
#You may assume that the height and weight entered will be positive integers.
#The program must print a message with the value of the Body Mass Index (BMI) rounded to two decimals and the category:
#Underweight = less than 18.5
#Normal = from 18.5 to 24.9
#Overweight = from 25 to 29.9
#Obesity = 30 or greater

def bmi_check(weight,height):
    # Convert centimeteres to meters
    height_meter = (int(height)/100);
    bmi = round(int(weight)/pow(height_meter,2));
    if bmi >= 30:
        return "Obesity";
    elif bmi < 29.9 and bmi > 25:
        return "Overweight";
    elif bmi < 24.9 and bmi >18.5:
        return "Normal";
    else:
        return "Underweight";


weight: int = input("Enter the weight in Kg: ");
height: int = input("Enter the height in centimeters: ");
print(bmi_check(weight,height));
