#Loops----Repetation of the task# excecute the block of code multiple times
"""
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

"""
"""
for i in range(1,3):
    print("hello world")

for i in range(0,10,2):
    print(i)
for i in range(1,10,2):
    print(i)

for i in range(-10,0,2):
    print(i)
for i in range(-1,-10,-1):
    print(i)
    
"""

for i in range(1,5):

    if i==2:
        print(i)
    else:
        print("no otput")

for i in range(1,5):
    print(i) # 1 2 3
    if i==3:
        break
for i in range(1,5):

    if i==3:
        continue
    print(i) # 1 2 4

for i in range(1,5):
    print(i) #1 2 3 4
    if i==3:
        continue

for i in range(1,10):
    if i==3 or i==5:
        print(i,end=" ")
    else:
        pass #no statement is needed

for i in range(0,11):
    if i%2==0:
      print(i) #2 4 6 8 10
    else:
        pass
for i in range(0,11):
    if i%2==0:
        continue
    else:
        print(i)  # 1 3 5 7 9



