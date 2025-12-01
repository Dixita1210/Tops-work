#Write a Python program to find the second smallest number in a list.


lst=[1,1,2,2,3,4,5,6,7,4,8,6]
second_smallest=sorted(set(lst))
print(second_smallest[1])

