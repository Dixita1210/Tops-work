24) Write a Python function to insert a string in the middle of a string. 

def insert_middle(main, word):
    middle = len(main) // 2
    new_string = main[:middle] + word + main[middle:]
    
    return new_string


print(insert_middle("HelloWorld", "Python"))

