"""
#square pattern
1. n=5
for i in range(1,6):
    for j in range(n,0,-1):
        print("*",end=" ")
    print("")
#hallow pattern
2. n=5
for i in range(0,5):
    for j in range(0,5):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
#right angle pattern
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
#left triangle pattern
3. n=5
for i in range(0,5):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")

    print("")
#pyramid pattern
4.n=5
for i in range(0,5):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print("")

#reverse pyramid
5.n=6
for i in range (6,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i):
        print("* ",end=" ")
    print("")
#reverse half pyramid pattern(left sided)
n=6
for i in range (6,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i):
        print("*",end=" ")
    print("")

        (or)
n=6
for i in range(1,6):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print("")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

#Half Diamond Pattern
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
n=6
for i in range(1,6):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print("")
# Reverse pyramid
n=int(input("enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
k=n
for i in range(1,5):
    for j in range(k-i,0,-1):
        print("*",end=" ")
    print("")
"""
#number patterns
"""
#1
n=5
num=1
for i in range(0,5):
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print("")
    
#2
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("") 
#3
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
    
"""

