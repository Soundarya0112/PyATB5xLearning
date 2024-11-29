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

dit={1:22,2:"anbbb",4:"apple","s":23}


# key existencey using in

print(22 in dit)

#another way of using dictionery

a = dict(name="a",b="c",age=20)  # ** unpacks the dictionary
print(a)


#mULTI DICTIONERY
stu1={"name":"aishu","age":24,"address":{"home address":"ppl","work address":"benguluru"}}
print(stu1)
stu2={"name":"soundu","age":23,"address":{"home address":"vjwada","work address":"vizag"}}
print(stu2)
stu3={"name":"aishu","age":24,"address":{"home address":"chennai","work address":"hyderabad"}}
print(stu3)

dict3=[stu1,stu2,stu3]
print(dict3)
print(dict3[0]) #{'name': 'aishu', 'age': 24, 'address': {'home address': 'ppl', 'work address': 'benguluru'}}
print(dict3[1]) #{'name': 'soundu', 'age': 23, 'address': {'home address': 'vjwada', 'work address': 'vizag'}}
print(dict3[0]["name"])#aishu
print(dict3[1]["address"])  #{'home address': 'vjwada', 'work address': 'vizag'}
print(dict3[2]["address"]["work address"])  #hyderabad


# Dictionery from two list
keys=["name","age","address","city"]
values=["Tara",23,"vjwda"]
dict4=dict(zip(keys,values))
print(dict4) #{'name': 'Tara', 'age': 23, 'address': 'vjwda'}

#merge two dictionary

d1={1:"a",2:"b"}
d2={3:"c",4:"d"}
print(d1|d2)


# to find the missing key

d3={1:"a",2:"b",6:"d"}
d4={3:"a",2:"b"}
missing_key=set(d3.keys())-set(d4.keys())
print(missing_key)
print(type(missing_key))

print(sorted(d3))