tup1=(1,2,3,"apple","banana","orange",2,2)
print(tup1)
print(type(tup1)) #tuple

tup2=("hi")
print(type(tup2))  #string

tup3=("hi",)
print(type(tup3)) #tuple
#1 indexing

print(tup1[1])
print(tup1[-1])
print(tup1[3:])
print(tup1[-1:])
print(tup1[2::2])
print(tup1[2::-1])

#Tuple methods
#1 concatination

print(tup1+tup3)
print((1,2,3)+(4,5,6))
print(("Hi",)*5)

#2.length
print(len(tup1))

#3 count
print(tup1.count(2))

#4 index

print(tup1.index("apple"))
print(tup1.index(1))

#5 deletion
#del tup2
print(tup2)

# for any modification in the items/obj in the tuple we need to convert to list and do it

#6

a=list(tup1)
print(a)

print(a.extend(["grapes","hello"]))
print(a)
print(tuple(a))

print(a.insert(0,"elephant"))
print(a)
print(tuple(a))

print(a.pop(1))
print(a)
print(tuple(a))


for i in a:
    print(i)