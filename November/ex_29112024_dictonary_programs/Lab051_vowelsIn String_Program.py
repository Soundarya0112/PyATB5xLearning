#count vowels in string
inp_str="aeiouse"

count=0
vowels="aeiou"
for each_char in inp_str:
    if each_char in vowels:

        count = count + 1
print(count)
