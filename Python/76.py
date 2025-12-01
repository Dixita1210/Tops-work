# Write a Python program to read a file line by line and store it into a list 

with open("AI.txt", "r") as file:
    content = file.readlines()
    print(content)

