# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
uniqlst=[]
for i in [1,2,3,2,3,4,5,6,4,5]:
    if i not in uniqlst:
        uniqlst.append(i)

print(uniqlst)