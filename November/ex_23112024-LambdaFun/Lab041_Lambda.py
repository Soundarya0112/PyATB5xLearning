num=int(input("enter the number:"))
def trip_fun(num):
    return num**3
result=trip_fun(num)
print(result)

#Lambda function: is an anonymous function returns some form of data
result=lambda num:num**3
print(result(3))


result=lambda a,b: a*b
print(result(2,4))

result=lambda a,b:a+b
print(result(2,3))

check_even_odd=lambda num:"even" if num%2==0 else "odd"
print(check_even_odd(45))

import math
result=lambda : math.pow(int(input("enter the number:")),2)
print(result()) #we always call a function