"""# maxium of 2 no's

x=float(input("enter the first number:"))
y=float(input("enter the Second number:"))
if x>y:
    print("x is maximum number",x)
else:
    print("y is maximum number",y)

#maxium of 3 no's

a=float(input("enter the first number:"))
b=float(input("enter the Second number:"))
c=float(input("enter the Third number:"))
if a>b and a>c:
    print("a is maximum number",a)
elif b>a and b>c:
    print("b is maximum number",b)
else:
    print("c is maximum number",c)
"""
s=int(input("enter your correct score:"))
if s>=90 and s<=100:
    print("A grade")
elif s>=80 and s<=89:
    print("B grade")
elif s>=70 and s<=79:
    print("C grade")
elif s>=60 and s<=69:
    print("D grade")
else:
    print(" Fail")

""" 
edge cases for above code is 
1.less than 60 marks
2.negtive score
3.if user entered string
4. if marks greater than 100

"""
