# Write a Python function to check whether a number is perfect or not.

num = int(input("Enter a number: "))

def is_perfect(number):
    if number < 1:
        return False  # perfect number is the number whose sum of dividors excluding the number itself are equal to number itself 
    
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    
    return sum_divisors == number

if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is NOT a perfect number")

