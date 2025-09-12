lst=[1,1,2,2,3,3,4,4,5,5,6,6,7,7]
lst_new=[]
for i in lst:
    if i not in lst_new:
        lst_new.append(i)
print(lst_new)