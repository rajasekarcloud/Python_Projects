# Challenge: Add a Key-Value Pair Only if the Key is Not in the Dictionary
# If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.
# Store the new key in the new_key variable and the new value in the new_value variable.
# Example 1: New Pair Added
# {"January": 45, "February": 56, "March": 67}
# "April": 67
# Output: {"January": 45, "February": 56, "March": 67, "April": 67}
# Example 2: No Change
# {"January": 45, "February": 56, "March": 67}
# The key already exists in the dictionary
# "January": 67
# Output: {"January": 45, "February": 56, "March": 67}
data = {"January": 45, "February": 56, "March": 67};
dict_key: str = input("Enter the key: ");
dict_value: int = int(input("Enter the value: "));
if dict_key not in data:
        data[dict_key] = dict_value;
else:
    print(f'{dict_key} already exist with the value {dict_value}');
print(data);
