# Can one block of except statements handle multiple exception? 

# Yes! In Python, one except block can handle multiple exceptions.

try:
    num = int(input("Enter a number: "))
    result = num/ 0
except (ValueError, ZeroDivisionError) as e:
    print("Error occurred:", e)
