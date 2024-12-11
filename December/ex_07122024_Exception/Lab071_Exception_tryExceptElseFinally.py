
try:
  a=int(input("enter the first no:"))  #value error if str entered
  b=int(input("enter the second no:"))
  c=a/b  #zerodivisionerror
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("result:",c)
finally:  #this block will always executes
    print("code executed successfully")

