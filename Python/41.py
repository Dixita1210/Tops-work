# #Write a Python program to check whether a list contains a sub list
#lst=[1,2,3,4,5,[6,7]]
lst=[1,2,3,4,5]

for i in lst:
    if type(i)==list:
      print('List has sublist')
      break
else:
   print('List does not sublist')


