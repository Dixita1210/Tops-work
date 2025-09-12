#append will add elements in the end of the list. It will add whole list as one element in previous list 

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
lst1.append(lst2)
print(lst1)

#extend will add single single elemets from one list to another 

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
lst1.extend(lst2)
print(lst1)
