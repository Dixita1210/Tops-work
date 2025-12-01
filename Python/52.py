# How Do You Check the Presence of a Key in A Dictionary

#using - 1) dict.keys()
#        2) dict.get(keys)

my_dict = {'a': 10, 'b': 20, 'c': 30}

user_input=input('Enter a key to find-')
if user_input in my_dict.keys():
    print('Key exists')
else:
    print('Key does not exists')