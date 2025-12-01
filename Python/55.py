# Write a Python script to merge two Python dictionaries 

dict1={'a' :1 , 'b' :2 }
dict2={'c' : 3, 'd': 4}
merged = dict1 | dict2
print(merged)

#another method 
dict1.update(dict2)
print(dict1)