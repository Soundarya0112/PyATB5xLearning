#heirarcial---1 parent and 2 or more child class
class Father:
    Land="2 acr"
    def house1(self):
        print("1 bhk")
class Navya(Father):
    def house2(self):
        print("no house")
class Aishu(Father):
    def house3(self):
        print("2 bhk")
class Soundu(Father):
    def house4(self):
        print("3bhk")
navya_obj=Navya()
print(navya_obj.Land)
navya_obj.house2()
navya_obj.house1()
#navya_obj.house3()
print("-----")
aishu_obj=Aishu()
print(aishu_obj.Land)
aishu_obj.house3()
aishu_obj.house1()
print("-----")
sow_obj=Soundu()
print(sow_obj.Land)
sow_obj.house4()
sow_obj.house1()

