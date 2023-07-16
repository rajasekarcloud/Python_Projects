# Challenge: Fahrenheit to Celsius Conversion
# The user should enter the degrees Fahrenheit.
# To convert degrees Fahrenheit to Celsius, we use this formula:
# <degrees_celsius> = (<degrees_fahrenheit> - 32) * 5/9
# The message should have this format:
# "<degrees> Fahrenheit = <degrees> Celsius"
# 77'F -> 25'C
fahrenheit: int = int(input("Enter Fahrenheit: "));
celcius = (fahrenheit - 32) * 5/9;
print(f'Fahrenheit {fahrenheit} -> Celsius {round(celcius,2)}');

