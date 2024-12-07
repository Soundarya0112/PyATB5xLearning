class Bank:
    def __init__(self,account_number,balance,name):
        self.name=name #public
        self.balance=balance #public
        self.__accountno=account_number #private
        self.__changeBalance=balance
    def display_privatevariable(self,isaut):
        if isaut==True:
            print(self.__accountno)
        else:
            print("autentication failed")
    def deposite(self,new_amount):
        self.balance=self.balance +new_amount
    def display(self):
        print(self.__changeBalance)
    def __display2(self): #private function
        print("hello everyone")
    def display3(self):
        self.__display2()

obj1=Bank(1234567891234,12000,"pinky")
print(obj1.name)
print(obj1.balance)
#print(obj1.__accountno)--we cannot access private variable directly
(obj1.display_privatevariable(True))
(obj1.display_privatevariable(False))
obj1.deposite(10000)
print(obj1.balance) #22000
#print(obj1.__changeBalance) #ee=rror
obj1.display()
#obj1.__display2()  --we cannot access private functionb directly
obj1.display3()