# Write a Python program to count the frequency of words in a file. 
from collections import Counter


with open("AI.txt", "r") as file:
    text = file.read()

words = text.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")


