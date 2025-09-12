# str1 = 'Dixita'

# print("D:", str1.count('D'))
# print("i:", str1.count('i'))
# print("x:", str1.count('x'))
# print("t:", str1.count('t'))
# print("a:", str1.count('a'))


str1='Dixita'
dict_freq={}
for i in str1:
    dict_freq[i]=str1.count(i)
print(dict_freq)

