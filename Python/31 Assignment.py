lst=['abc','xyz','a','bc','aba','babab','xyxz','1221','wow']
c=0
for i in lst:
    if len(i)>=2 and i[0]==i[-1]:
        c+=1
print(c)