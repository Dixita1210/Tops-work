#Write python program that user to enter only odd numbers, else will raise an exception. 


n = int(input("Enter an odd number: "))

if n % 2 == 0:
    raise Exception("This is not an odd number! Please enter only odd numbers.")
else:
    print("Thank you! You entered an odd number:", n)
