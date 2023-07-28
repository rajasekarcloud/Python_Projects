# Challenge: Count Vowels in a String
# Write a Python program that counts the number of vowels in a string recursively.
# If the string is empty or only contains one consonant, print 0.
def count_vowels(word):
    word = word.lower();
    if word[0] in ["a","e","i","o","u"]:
        return 1 + count_vowels(word[1:]);
    else:
        return count_vowels(word[1:]);
    
print(count_vowels("welcome"));
