"""
# 1.
a=10
def my_fun():
    b=20
    print(a)
    print(b)
#print(b) #local variable can't access outside
print(a)#global variable can access outside and inside
my_fun()

# 2.
a=10
def my_fun():
    b=20
    print(b)
    a=30
    print(a) #local variable has more preference than global variable
my_fun()

"""
# 3

def outer_fun():
    var1 = 30

    def inner_fun1():
        var2=50
        print(var1)
        print(var2)
    def inner_fun2():
        print(var1)
       # print(var2)#1 local variable can't access inside other local variable
    inner_fun1()
    inner_fun2()
outer_fun()
#inner_fun1() #local variable can't access outside




