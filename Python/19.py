19) Write a Python program to count the occurrences of each word in a  

str='Hello Good Good Morning Hello '
dict_freq={}
word=str.split() #here split will give output in a list so we have to iterate tge word variable with i
for i in word:
    dict_freq[i]=str.count(i)
print(dict_freq)

