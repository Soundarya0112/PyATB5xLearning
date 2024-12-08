#multilevel--GF>F>C
class GrandFather:
    silver="2kg"
    def house1(self):
        print("2bhk")
class Father(GrandFather):
    gold="3kg"
    def house2(self):
        print("3bhk")
class Child(Father):
    diamond="5kg"
    def house3(self):
        print("4bhk")
child_obj=Child()
print(child_obj.diamond)
print(child_obj.gold)
print(child_obj.silver)
child_obj.house3()
child_obj.house2()
child_obj.house1()
print("------")
father_obj=Father()
print(father_obj.gold)
print(father_obj.silver)
#print(father_obj.diamond)--father cannot access child  attribute/methods he can access his class and his parent class
father_obj.house2()
father_obj.house1()

print("------")
Grandfather_obj=GrandFather()
print(Grandfather_obj.silver)
#print(Grandfather_obj.gold)--GF cannot access  his child class attributes
#print(Grandfather_obj.diamond)--gf cannot access  his child class attributes
Grandfather_obj.house1()
#Grandfather_obj.house2()--gf cannot access  his child class methods
