# Challenge: Check if All Values are Equal
# Write a Python program that checks if all values in a dictionary are equal.
#
# If they are, print True. Else, print False.
#
# If the dictionary is empty, print "Empty".
# {"a":4,"b":4","c":4} = True
# {} = Empty
# {"a":4,"b":5"} = False
dict = {"a":4,"b":4,"c": 4};
if dict == {}:
    print(f'Empty Dict');
else:
    if len(set(dict.values())) > 1: # Set return unique elements
        print(f'False');
    else:
        print(f'True');
