dict1={1,}
print(dict1)
print(type(dict1)) #set

dict1={}
print(dict1)
print(type(dict1))  #dict

dict1={1:"a",2:"apple",3:"orange",4:"grapes",1:"abc"}
print(dict1)
print(type(dict1))


#dict methods

#1 keys
print(dict1.keys())

#2 values
print(dict1.values())

#get
print(dict1.get(4))

#copy()
dict2=dict1.copy()
print(dict2)

#items
print(dict1.items())

#pop
print(dict1.pop(1))
print(dict1)

#popiteam  by default last
print(dict1.popitem())
print(dict1)

#update
print(dict1.update({0:"zebra",1:"hi"}))
print(dict1)

#sorted
print(sorted(dict1))
print(dict1)

#clear
#print(dict1.clear())
print(dict1)

#updating values

dict1[2]="watermelon"
print(dict1)