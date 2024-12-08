class Mother:
    gold="2kg"
    def properties(self):
        print("2bhk home and 10 acer field")
class Father:
    land="100 cent"
    def properties(self):
        print("3 bhk home")
class child(Mother,Father):
    def display(self):
        print("i'm child class")
child_obj=child()
print(child_obj.gold)
print(child_obj.land)
child_obj.properties()  #if methods are same for father and mother then first mentioned one will print as output
child_obj.display()