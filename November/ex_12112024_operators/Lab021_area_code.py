import math
pi=math.pi
r=int(input("enter the radius value:"))
area=pi*pow(r,2)
print("area of the circle is", area)

# Usetheternary operator to find the maximum of three numbers entered by the user

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the Third number:"))
print("a is max num" if a>b and a>c   else "b is max" if a<b and c<a else "c is max")
