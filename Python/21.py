21) Write a Python program to add 'in' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged. 

    str=input('Enter a string-')
if len(str)<3:
    print(str)
elif str.endswith('ing'):
     print(str.replace('ing','ly'))
else:
    print(str+'in')

