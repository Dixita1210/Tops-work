# Write a Python program to count the number of lines in a text file. 
with open("AI.txt", "r") as file:
    line_count = 0  
    for line in file:
        line_count += 1  

print("Total number of lines in the file:", line_count)
