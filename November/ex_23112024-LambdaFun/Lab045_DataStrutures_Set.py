set1={1,2,3,3,3,2,5,"hello","apple","elephant"}
print(set1)
print(type(set1))

set2={1,}
print(type(set2))

set3={}
print(type(set3))
set4=set()  #empty set
print(type(set4))

seta={1,2,3,5,6,7}
setb={2,3,7,"a","b"}
print(seta|setb)
print(seta&setb)
print(seta-setb)
print(setb-seta)

#set methods

#1 ADD

seta={1,2,3,5,6,7}
(seta.add(12))
print(seta)

#2 remove

seta.remove(7)
print(seta)

#3 pop

seta.pop()
print(seta)

#4 discard
seta.discard(6)
print(seta)

#5 copy
setc=seta.copy()
print(setc)

#clear

seta.clear()
print(seta)

#issuperset and subset

print(seta.issubset(setb))
print(seta.issuperset(setb))
print(setb.issuperset(seta))
