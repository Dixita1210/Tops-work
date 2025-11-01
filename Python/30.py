30) How will you compare two lists? 

lst1=[1,2,3,4]
lst2=[4,5,6,7]

#convert into set and use the function 

lst_new=set(lst1).intersection(set(lst2))
print(lst_new)

lst_new=set(lst1).difference(set(lst2))
print(lst_new)

lst_new=set(lst2).difference(set(lst1))
print(lst_new)



