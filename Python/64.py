# Write a Python function that checks whether a passed string is palindrome or not 
# A palindrome is a word, phrase, or number that reads the same forward and backward.


def is_palindrome(s):
    s = "".join(ch for ch in s.lower() if ch.isalnum()) #remove space and punchuation and convert to lowercase 
    return s == s[::-1] #reverse slicing 

word = input("Enter a string: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
