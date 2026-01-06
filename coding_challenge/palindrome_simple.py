def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
# : → take the whole string
#
# -1 → step backwards
#
# [::-1] → read the string from end to start
print(is_palindrome('kayak'))
