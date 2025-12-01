#Write a Python function that takes two lists and returns true if they have at least one common member.

lst1=[1,2,3,4,5,6,7,8]
lst2=[1,1,2,3,4,5,6]
for i in lst1:
    if i in lst2:
        print('True')
        break
else:
  print('False')