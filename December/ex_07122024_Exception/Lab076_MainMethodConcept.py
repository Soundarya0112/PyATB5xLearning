def main():
    print("this name can be anything method1")
def main_name_can_be_anything():
    print("this name can be anything method2")
if __name__=="__main__":  #python interpreter understand that main method,if we call like this statement
    main()
    main_name_can_be_anything()

#ex2
print("----------------")

def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
def f4():
    print("f4")
def main():
    print("main method printed")
if __name__=="__main__":
    main()
    f1()
    f2()
    f3()
    f4()
