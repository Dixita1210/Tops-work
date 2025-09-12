#Swap with using temp variable 
x=12
y=13
temp=x
x=y
y=temp
print("The value of x is", x)
print('The value of y is', y)

#Swap without using temp variable 
x=12
y=13
x,y=y,x
print("The value of x is", x)
print('The value of y is', y)
