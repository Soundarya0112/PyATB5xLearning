#functions: block of reusebilty code that performs specific task
#function with no argument


#1. No return type no argument
def greet():
    print("hello universe")
    print("hi")
    print("hello")
greet()
greet()
print("abcdefgh")
greet()

#2. no return type with argument
#function with argument
def greet(name):
    print("hello",name)
greet("soundarya")
name="aishwarya"
greet(name)

#3 No return type defult argument

def greet(name1="pinky",name2="tara"):
    print("hello", name1,name2)
greet()
greet(name1="soundu")
greet(name2="aishu")

#4 argument+returntype

def sum(a,b):
    return a+b
sum_result=sum(30,40)
print(sum_result)

#argument+returntype with defult

def sum(a=20,b=30): # it takes default if no parameturs called
    return a+b
result=sum(a=100,b=200)
print(result)
result=sum()
print(result)



