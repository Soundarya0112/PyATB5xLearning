class Parent:
    gold="2kg"
    def house(self):
        print("2bhk")
class child(Parent):
    diamond="3kg"
    def house2(self):
        print("3bhk")
parent_obj=Parent()
print(parent_obj.gold)
parent_obj.house()
print("-----")
child_obj=child()
print(child_obj.diamond)
print(child_obj.gold)
child_obj.house2()
child_obj.house()
#parent_obj.house2()--parent class cannot access child attributes or methods,only child class can
                      # access both parent and it's own child class