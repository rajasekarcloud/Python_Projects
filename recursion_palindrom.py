# Challenge: Check if a String is a Palindrome
# Print True if the string is a palindrome. Else, print False.
def palindrome(word):
    if len(word) <= 1:
        return True;
    elif word[0] != word[-1]:
        return False;
    else:
        return palindrome(word[1:-1]);

print(palindrome("MalayalaM"));
