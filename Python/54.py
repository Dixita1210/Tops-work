# Write a Python program to check multiple keys exists in a dictionary 


my_dict = {'name': 'Dixita', 'age': 25, 'city': 'Delhi'}

keys_to_check = ['name', 'age']

if all(key in my_dict for key in keys_to_check):
    print("All keys exist")
else:
    print("One or more keys are missing")


