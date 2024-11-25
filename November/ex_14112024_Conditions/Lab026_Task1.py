# Triangle classifier

s1 = int(input("enter the length of the first side:"))
s2 = int(input("enter the length of the second side:"))
s3 = int(input("enter the length of the Third side:"))
if s1==s2==s3 :
    print("equilateral triangle")
elif s1 ==s2 or s1 == s3 or s2 ==s3 :
    print("isosceles triangle")
else:
    print("scalene triangle")


a=float(input("enter the a value:"))
b=float(input("enter the b value:"))
c=float(input("enter the c value:"))

def classify_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and b+c>a and c+a>b:#triangle condition
            if a==b==c:
                return "equilateral "
            elif a==b or a==c or b==c:
                return "isosceles"
            else:
                return "scalene"
        else:
            print("not a triangle")
    else:
        print("not a valid length")
result=classify_triangle(a,b,c)
print(result)