#5) Write a Python program to get the Factorial number of given numbers.

    num=int(input('Enter a number-'))
fac=1    #here fac is a variable where the factorial will be stored. It can not be zero because the i will  be multiplied with 0 and answer will be 0 
for i in range(1,num+1):
    fac=fac*i
print('Factorial of given number is',fac)



