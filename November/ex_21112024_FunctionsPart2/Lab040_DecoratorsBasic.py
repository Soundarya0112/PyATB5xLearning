#a decorator is a design pattern that allows you to modify or extend the behavior of functions or methods
# without changing their actual code.


def dec_fun(fun):
    def wrapper_fun():
        print("before calling the function")
        fun()
        print("after calling the function")
    return wrapper_fun
@dec_fun
def greet():
    print("hello")
greet()