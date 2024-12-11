#customException

class LowBalanceException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)
balance=100
withdraw=int(input("enter the money to withdraw:"))
if withdraw>balance:
    raise LowBalanceException("UR BALNCE IS LOW,PLS CHECK")
else:
    print("Remaining bal:",balance-withdraw)