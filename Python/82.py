 # Write a Python program to copy the contents of a file to another file. 


with open('newfile.txt', 'r') as source_file:
    content = source_file.read()  


with open('newfile2.txt', 'w') as dest_file:
    dest_file.write(content)  

print("File copied successfully!")
