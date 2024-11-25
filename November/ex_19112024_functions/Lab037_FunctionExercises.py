# 1 Python function to find the maximum of three numbers
"""
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
def max_of_3(a=100,b=200,c=300):
    if a>b and a>c:
        print("a is maximum")
    elif b>a and b>c:
        print("b is maximum")
    else:
        print("c is maximum")
max_of_3(a,b,c)
max_of_3()#it takes default parameters

#2 Factorial of a number
n=int(input("enter the number:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(n)
print(result)
result=factorial(5)
print(result)

# 3 Fibonacci Sequence
n = int(input("enter the number:"))


def fibonacci(n):
    fib_seq = []
    if n == 0:
        return fib_seq
    #fib_seq.append(0)
    if n == 1:
        return [0]
    #fib_seq.append(1)
    fib_seq=[0,1]


    for i in range(2, n):
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
    return fib_seq
result = fibonacci(n)
print(result)
"""

#4 Prime Number Checker
def prime_check(n):
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
result=prime_check(3)
print(result)