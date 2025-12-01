# Find the length of the longest word in  a  file

with open("AI.txt", "r") as file:
    text = file.read()  
words = text.split()  
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
longest_words = []
for word in words:
    if len(word) == max_length:
        longest_words.append(word)
print("Length of the longest word:", max_length)
print("Longest word(s):", longest_words)
