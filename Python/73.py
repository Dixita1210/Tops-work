# Append text to file
file = open("newfile.txt", "a")
file.write("\nThis is new appended text.")
file.close()

# Now read and display the file
file = open("newfile.txt", "r")
print(file.read())
file.close()
