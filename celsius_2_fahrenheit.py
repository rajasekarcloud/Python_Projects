# Challenge: Celsius to Fahrenheit Conversion
# To convert degrees Celsius to Fahrenheit, we use this formula:
# <degrees_fahrenheit> = (<degrees_celsius> * 9/5) + 32
# The message should have this format: "<degrees> Celsius = <degrees> Fahrenheit"
celsius: int = int(input("Enter Celsius: "));
fahrenheit = (celsius * 9/5) + 32;
print(f'Celsius {celsius} -> Fahrenheit {round(fahrenheit,2)}');
