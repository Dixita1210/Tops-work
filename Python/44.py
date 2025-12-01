#Write a Python program to create a tuple with different data types.

tpl = (10, 3.14, "Hello", True, [1, 2, 3], (4, 5), {'name': 'Dixita', 'age': 25})
for i in tpl:
      print(f"Value: {i}, Type: {type(i)}")