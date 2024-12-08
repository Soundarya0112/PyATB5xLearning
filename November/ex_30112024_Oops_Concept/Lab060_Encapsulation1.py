#Encapsulation --we can restrict access to variables and methods/function
# wrapping or binding the data variables with the methods called encapsulation
#private through  __(underscore)
class WebPage:
    def __init__(self,name,password):
        self.name=name  #public
        self.password=password #public
        self.__password=password
    def display_private(self,is_autentication):
        if is_autentication==True:
            print(self.__password)
        else:
            print("autentication failed,pls try again")

obj1=WebPage("pinky","sow123$")
print(obj1.name)
print(obj1.password)
#print(obj1.__password) # error---we cannot access private variable/attribute directly --we can use trhe function
obj1.display_private(True)
obj1.display_private(False)
