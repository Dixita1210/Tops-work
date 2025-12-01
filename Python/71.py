# What is File function in python? What are keywords to create and write file. 

#Python provides built-in file handling functions that allow you to:
#                                                   Create files
#                                                   Open files
#                                                   Read files
#                                                   Write to files
#                                                   Append data
#                                                   Close files

#keywords to create and write a file -

f = open("newfile.txt", "x")
f.write("New file created.")
f.close()

f = open("myfile.txt", "w")
f.write("Hello!")
f.close()
