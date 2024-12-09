#static method--it is method that belongs to class rather than a instance of the class
class Operations:
    @staticmethod
    def sum(a,b):
        print("sum:",a+b)
    def sub(self,a,b):
        print("sub:",a-b)
#no need to create object for static methods
Operations.sum(2,4)
O1=Operations()
O1.sub(5,1)

#we can have n no of static methods