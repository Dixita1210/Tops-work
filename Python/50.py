 #Write a Python script to check if a given key already exists in a dictionary. 

dict = {'a': 1, 'b': 4, 'c': 2}
# user_input=input("Enter a key-")
# if user_input in dict.keys():
#     print('Key exists')
# else:
#     print('Key does not exists')

if dict.get('b') is not None:
    print('key exists')
else:
    print('key does not exists')