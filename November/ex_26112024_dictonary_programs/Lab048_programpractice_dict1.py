#write a program to find the frequency of each character
from os import remove

str1=input("enter the string:")
def fre_caluclation(str1):
    dict={}
    for each_char in str1:
         if each_char in dict:
             dict[each_char]+=1
         else:
             dict[each_char]=1
    return dict
a=fre_caluclation(str1)
print(a)

#function that return the maximum value from a dictionary

def maximum_value(dict1):

    #return max(dict1.values())
    return min(dict1.values())
b=maximum_value({1:23,3:100,4:1000})

print(b)


#remove duplicates from the dictionary

my_dict={"a":1,"b":2,"c":1}
#output={"a":1,"b":2}

unique_set=set() #empty set
dict={}
for key,value in my_dict.items():
     print(value)
     if value not in unique_set:
          print(value)
          dict[key]=value
          unique_set.add(value)
print(dict)

