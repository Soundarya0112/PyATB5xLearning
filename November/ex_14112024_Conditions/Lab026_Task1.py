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
