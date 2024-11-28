a="soundarya" #double quote
b='aishu' #single quote
c="""hi soundarya how are  
you? where are u 
 from?"""#multiline string with triple quote
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#1 string indexing
print(a[5])
print(a[-2])
print(a[6]) #string index out of range
#2 String slicing
print(a[:])
print(a[0:5])
print(a[:7])
print(a[5:])
print(a[:-1])
print(a[-3:])
print(a[0::-2])
print(a[2::-1])

#3 string assign

#print(a[0]="a") #not possible to change

#4 string del
#del c
print(c)

#5 String operations

a="soundarya"
print(a*4)
print(a+"1")
#print(a+1) #we get error string to int concatination
print(a+" "+b)

print("s" in a)
print("o" in a)
print("z" in a)

#6 String formating

print("{} and {} both are enemies".format("kavya","navya"))
print("{a} and {b} both are enemies".format(b="kavya",a="navya"))
print("{1} and {0} both are enemies".format("kavya","navya"))
name="pinky"
salary=100000
print("her name is %s and her salary is %d"%(name,salary))

#7 string functions

s1="pYtHon ProGramming"
print(s1.lower())
print(s1)
s2=s1.lower()
print(s2)

print(s1.upper())
print(s1)
s2=s1.upper()
print(s2)

print(s1.title())
print(s1)
s2=s1.title()
print(s2)

print(s1.casefold())
print(s1)
s2=s1.casefold()
print(s2)

print(s1.count("o"))
print(s1)
s2=s1.count("o")
print(s2)

print(s1.replace("pYtHon","java"))
print(s1)
s2=s1.replace("pYtHon","java")
print(s2)

print(s1.index("o"))
print(s1)
s2=s1.index("o")
print(s2)

print(s1.split())
print(s1)
s2=s1.split()
print(s2)

print(s1.capitalize()) #only first letter capital
print(s1)
s2=s1.capitalize()
print(s2)


print(len(s1))
