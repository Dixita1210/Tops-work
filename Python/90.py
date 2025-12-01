#Write python program that user to enter only odd numbers, else will raise an exception. 


try:
    n=int(input('Enter a number -'))
    if n%2==0:
        raise ValueError('This is not an odd number ')
    print('This is an odd number')
except ValueError as e:
    print('Error:', e)