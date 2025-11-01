31) Write a Python program to count the number of strings where the string  
length is 2 or more and the first and last character are same from a given list 
of strings. 

lst=['abc','xyz','a','bc','aba','babab','xyxz','1221','wow']
c=0
for i in lst:
    if len(i)>=2 and i[0]==i[-1]:
        c+=1

print(c)
