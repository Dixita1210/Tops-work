 # Write a Python program to write a list to a file. 


lst = ["Python", "AI", "Machine Learning", "Data Science"]


with open("newfile3.txt", "w") as file:
    file.write(str(lst))

print("List written to file successfully!")
