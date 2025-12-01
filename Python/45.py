# Write a Python program to unzip a list of tuples into individual lists. 

data = [(1, 2), (3, 4), (5, 6)]
list1, list2 = zip(*data)

print("List 1:", list(list1))
print("List 2:", list(list2))

   