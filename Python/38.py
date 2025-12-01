#Write a Python program to select an item randomly from a list. 

import random
# lst=[1,2,3,4,5,6,7,8]
# a=random.choice(lst)
# print(a)

lst=[1,2,3,4,5,6,7,8]
for i in lst:
    a=random.randint(0,len(lst)-1)
print(a)