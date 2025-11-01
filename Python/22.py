22) Write a Python function to reverses a string if its length is a multiple 
of 4. 

    user_input = input('Enter a string- ')
if len(user_input) % 4 == 0:

    print(user_input[::-1])
else:
    
    print(user_input)

