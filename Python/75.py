# Write a Python program to read last n lines of a file.n = int(input("Enter number of lines to read from the end: "))

n = int(input("Enter number of lines to read from the end: "))

with open('AI.txt', 'r') as file:
    lines = file.readlines()      
    last_lines = lines[-n:]       
    for line in last_lines:
        print(line, end='')
