a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
def sum_of_3num(a=100,b=200,c=300):
    return a+b+c
result=sum_of_3num()
print(result)
result=sum_of_3num(a,b,c)
print(result)
result=sum_of_3num(a,20,300)
result=sum_of_3num(a)
print(result)
print(result)

def multiple_args(*args):
    #*args--gives list--we can iterarte using for loop---we can have any no of arguments
    for i in args:
        print(i)
multiple_args("sow","aish","navi")
multiple_args("a","b","c","d",1,2,3,5)
