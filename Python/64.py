# Write a Python function that checks whether a passed string is palindrome or not 
# A palindrome is a word, phrase, or number that reads the same forward and backward.


def is_palindrome(s):
    if s == s[::-1]: #reverse slicing 
        return True
    else:
        return False

word = input("Enter a string: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

string_input = input("Enter a string: ")
if string_input== string_input[::-1]:
    print(f'{string_input} is a palindrome')

else:
    print(f'{string_input} is a not palindrome')