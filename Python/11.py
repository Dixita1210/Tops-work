11) Write a Python program to test whether a passed letter is a vowel 
or not. 

user_input=input('Enter a letter-')
vowels=('a','e','i','o','u')
if user_input in vowels:
    print(f'{user_input} is a vowel' )
else:
    print(f'{user_input} is not a vowel ')

