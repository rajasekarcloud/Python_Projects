def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): # Skip non alpha numericals
            left += 1

        while left < right and not s[right].isalnum(): # Skip non alpha numericals
            right -= 1
        print(s[left].lower(),s[right].lower())

        if s[left].lower() != s[right].lower():
            return False # Not a palindrome

        left += 1
        right -= 1
        print(left, right)

    return True
print(is_palindrome('hello'))
---------------------------------


def is_palindrome(s):
    # Assign left and right
    left, right = 0, len(s)-1
    # Check if there are any non alpha nums
    while left < right and not s.isalnum():
        left +=1
        right -=1
        if s[left] != s[right]:
            return "Not A Palindrome"
    return "Palindrome"

print(is_palindrome('hello'))
