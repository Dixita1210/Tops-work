# Write a Python program to read first n lines of a file



n = int(input("Enter number of lines to read: "))

with open('AI.txt', 'r') as file:
    lines = file.readlines()
    for i in lines[:n]:
        print(i, end='')
