# Write a Python function to calculate the factorial of a number (a nonnegative integer) 
num=int(input('Enter a number ='))

def factorial(n):
    if n<0:
        raise ValueError ('Factorial of negative number is not possible')
    result= 1
    for i in range(1,n+1):
        result *=i
    return result


print(f'Factorial of {num} is {factorial(num)}')