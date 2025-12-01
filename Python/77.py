# Write a Python program to read a file line by line store it into a variable.

with open("AI.txt", "r") as file:
    content = file.readlines()
    # print(content)

a=content
print('a=', a)
