a=10 #global variable
class Practice:
    b=11  #instance variable--within the class
    def print_fun(self):
        c=5  #local variable
        #print(self.c) #wont print--error---local variable can access directly
        print(c)
       # print(b) #wont print--error---instance variable can access with self
        print(self.b)
        global a
        print(a)
        a="hello"
        print(a)  #local variable has more preference than global

obj_ref=Practice()
obj_ref.print_fun()