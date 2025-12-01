#When will the else part of try-except-else be executed?
 
 
 # In Python, the else block in a try-except-else structure 
 # is executed only if no exception occurs in the try block.


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered a valid number:", num)
