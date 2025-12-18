# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def unique_list(lst):
    new_list = []              
    for item in lst:
        if item not in new_list:  
            new_list.append(item) 
    return new_list
print(unique_list([1, 2, 2, 3, 4, 4, 5]))
