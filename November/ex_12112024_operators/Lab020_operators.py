age = 20
print(age)
"""
age->identifier --variable name
20->literal--variable value
=->assignment operator
"""
#Assignment operator--> =,+=,-=,*=,/=,%=
a=11
print(a)
a+=1  #a=a+1=12
print(a)
a-=1  #a=a-1=11
print(a)
a*=1  #a=a*1=11
print(a)
a/=1  #a=a/1=11.0
print(a)
a%=1  #a=a%1=0.0
print(a)

# unary operator--> ++,--
age1=+30
print(age1)
age2=-30
print(age2)
"""
+30, -30
here +, - is the
unary
operator - -it is added
to
one
operand
1)UnaryOperator
○ Onlyoneoperandisrequired.
● 2)BinaryOperator
○ Twooperandsarerequired.
"""



age3=1
age3+=1#or
age3=age3+1
print(age3)

#Arthimetic operator---  +,-,*,/,%
a=20
print(a+20)
print(a-20)
print(a*20)
print(a/20)

# %,// operators
"""
% ---modulas
operator(gives
Remainder)
// -- floor division(gives quotient)
"""

print(13//2)#--quotient
print(13/2)#--div
print(13%2)#remainder

# power operator

print(2**4)
a=2
print(a**2)
print(pow(2,4))

#comparision operator

print(2==3)
print(2==2)

#logical operator-->or,and,not(!)
a=10
b=20

print(a==10 and b==8)
print(a==10 or b==8)
print(a!=b)

#Not operator
iloveindia=1 #or u can use True here
iloveindia=True
print(not iloveindia )# answer=False

#Relational operator--> <,>,<=,>=,==,!=

a=10
b=20
c=10
print(a>b)#False
print(a<b)#True
print(a>=c)#True
print(a<=b)#True
print(a!=b)#True
print(a==b)#False


#Terniray operator-- depends on if else

a=10
b=20
print("a is smaller" if a<b else "a is larger")

age=int(input("enter ur correct age:"))
print("u can go for vote" if age>18 else "u cannot vote")

#bit wise operat --> (&,|,~,>>,<<,^)
a=10#1010
b=2#0010
print(a&b)#0010=2
print(a|b)#1010=10
print(~a)#0000 1010  --> 1111 0101-> add1 to original bit  1011=-11
print(~b)# 0000 0010 -->1111 1101-->add1 to original bit  0011=-3
print(a>>1)#0101=5-->10//2 pow1 =5
print(a>>2)#0010=2-->10// 2 pow 2=2
print(a<<1)#10100=20-->10* 2pow 1=20
print(a<<2)#101000=40--> 10* 2 pow 2=40