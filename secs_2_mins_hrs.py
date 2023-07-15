# Challenge: Convert Seconds to Minutes and Hours
# Present the minutes as an integer and the hours as a decimal value.
# 5400 seconds is equivalent to:
# 90 Minutes
# 1.5 Hours
sec: int = int(input("Enter seconds: "));
if sec == 0:
    print('0 Hrs and 0 Mins');
else:
    mins = round(sec/60,2);
    hrs = round(sec/60/60,2);
    print(f'{sec} seconds = {hrs} Hrs');
    print(f'{sec} seconds = {mins} Mins');
