# we can use exception in class as well

class XYZ:
    def ex(self):
        try:
            a=int(input("enter a number:"))
        except Exception as e:
            print(e)
        else:
            print(a)
        finally:
            print("i will be printer always")
o1=XYZ()
o1.ex()