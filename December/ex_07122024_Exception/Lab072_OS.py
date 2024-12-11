import  os
print(os.getcwd()) #current working directory

#list files in the currect directory
files=os.listdir("/Users/soundarya/Desktop/python Automation/PyATB5xLearning")
print(files)

#create directory
#os.mkdir("January")

#check file exists
file_exist=os.path.exists("abc.txt")  #True
print(file_exist)
print(os.name)  #nt--windows, posix--mac

import os
try:
    full_path=os.getcwd()
    print(full_path)
    file=open(full_path)
except Exception as e:
    print(e)
finally:
    print("close")
