 #Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

# Sort values in ascending order
asc_vales = sorted(my_dict.values())
print(asc_vales)

sorted_dict_asc = {}

for value in asc_vales:
    for key in my_dict:
        if my_dict[key] == value and key not in sorted_dict_asc:
            sorted_dict_asc[key] = value

print("Ascending:", sorted_dict_asc)


#  Sort values in descending order
desc_values =asc_vales[::-1]   

sorted_dict_desc = {}

for value in desc_values:
    for key in my_dict:
        if my_dict[key] == value and key not in sorted_dict_desc:
            sorted_dict_desc[key] = value

print("Descending:", sorted_dict_desc)



