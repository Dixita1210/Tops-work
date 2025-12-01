# Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.

str='Dixita'
dict1={}

for i in str:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)