#Right Triangle Star Pattern
n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

#Left Triangle Star Pattern
n=int(input("enter the value:"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
