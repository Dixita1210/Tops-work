str=input('Enter your string-')
str_mid=input('Enter your middle string-')
mid=len(str)//2
str_new=str[:mid]+str_mid+str[mid:]
print(str_new)
