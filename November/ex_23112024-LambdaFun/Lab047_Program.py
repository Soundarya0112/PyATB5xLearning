# finding the first non repet=ating character in a  string using sets

set1=input("enter the string: ")
def non_repeating_string(set1):
    for char in set1:
        if set1.count(char)==1:
            return char
        else:
            None
result=non_repeating_string(set1)
print(result)
result=non_repeating_string("daddy")
print(result)


