list1=["a",1,2,"bcd",39,"pinky"]
print(list1)
print(type(list1))

print(len(list1))
#1 List indexing

print(list1[0])
print(list1[3])
print(list1[-2])

#2 list slicing
print(list1[1:4])
print(list1[::-1])
print(list1[0::-1])
print(list1[2::-1])
print(list1[::-2])
print(list1[3][1])

#3 list methods
print(list1.append("aishu")) #none
print(list1) #print correct list
list2=list1.append("banana")
print(list2)  #none

list1.insert(0,"apple")
print(list1)

list1.extend([1,2,"hi"])  #we can add list
print(list1)

print(list1.index("aishu"))   #index of the element
print(list1)

(list1.remove("hi"))  #remove that element
print(list1)

list1.pop()  #last element will delete
print(list1)

list1.pop(0)  #0 index element will delete
print(list1)



list1.reverse()  #reverse the list
print(list1)

#del list1
print(list1)

list1.clear()  #empty list
print(list1)

list1=[90,8,0,-1,1,1,1]  # ascending order sort
list1.sort()
print(list1)

print(list1.count(1)) #count the no of occurnce of that element
print(list1)

list2=(list1.copy())  #copy of the list
print(list2)

