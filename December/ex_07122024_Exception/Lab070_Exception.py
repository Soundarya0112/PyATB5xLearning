"""
 #x=10   #indentation error
#print(10/0) #ZeroDivisionError
#print(1+"a") #TypeError  --unsupported operand type(s) for +: 'int' and 'str'
#print(int("a"))  #ValueError--invalid literal for int() with base 10: 'a'
a=[1,2,3,4]
print(a[10])  #IndexError: list index out of range

if a==10;
    print(a)  #SyntaxError: invalid syntax

try:
    try this code if error
except:
    execute me if try has some error
"""
from logging import exception

print("start program")
try:
  a=int(input("enter the first no:"))  #value error if str entered
  b=int(input("enter the second no:"))
  c=a/b  #zerodivisionerror
  print("result is: ",c)
except Exception as e:
    print(e)
print("end of the program")

print("-------------------------------")
import math
try:
   math.pow(1000,10000)
except Exception as e:
    print("Error is",e)

