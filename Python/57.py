 # Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 50, 'b': 20, 'c': 70, 'd': 10, 'e': 90}
highest_3 = sorted(my_dict.values())[-3:] #slicing 
print(highest_3) #output is in list 