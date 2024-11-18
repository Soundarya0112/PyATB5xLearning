"""
#Print first 10 natural numbers using while loop
i=1
while i<=10:
    print(i)
    i=i+1

#Calculate sum of all numbers from 1 to a given number
a=int(input("enter the number:"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

#Print multiplication table of a given number
n=int(input("enter the number:"))
for i in range(1,11):
    p=n*i
    print(2,"x",i,"=",p)

#Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)
    
#Calculate the cube of all numbers from 1 to a given number:
num=int(input("enter a number:"))
for i in range(1,num+1):
    cube=i**3
    print(cube)

"""
#Print all prime numbers
for num in range(1,10): #2 3 5 7
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


#Print the following pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
"""
i=1 j=1
i=2 j=1 2
i=3 j=1 2 3 
i=4 j=1 2 3 4
i=5 j=1 2 3 4 5
"""
#Print the following pattern
for i in range(0,6):
   for j in range(5,i,-1):
       print(j,end=" ")
   print("")
#Print the following pattern
k=5
for i in range(0,6):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print("")