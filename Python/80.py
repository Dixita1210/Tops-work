# Write a Python program to count the frequency of words in a file. 
with open("AI.txt", "r") as file:
    text = file.read()  
words = text.split()  #splitting words from sentence
word_count = {}       #create new dict to store word and count
for i in words:
    if  i in  word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
for i, count in word_count.items():
    print(f"{i}: {count}")
