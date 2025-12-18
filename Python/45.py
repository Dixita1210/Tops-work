# Write a Python program to unzip a list of tuples into individual lists. 

data = [(1, 2), (3, 4), (5, 6)]
list1, list2 = zip(*data)  #zip will pair 1st elemets together and 2nd elements together thats why we have two list here 

print("List 1:", list(list1))
print("List 2:", list(list2))


   
