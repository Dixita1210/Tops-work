 #How Do You Handle Exceptions with Try/Except/Finally in Python? 

try:
    no=input('Enter a number-')
    no1=int(no)
    print(f'value is {no1}')

    ans=no1/0
    print(f'Ans {ans}')

except ZeroDivisionError:
    print('There is a zero divison error')  

except ValueError:
    print('There is a value error')

finally:
    print('Have a great day')
