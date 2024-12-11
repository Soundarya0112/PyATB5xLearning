import os

filename="pinky.txt"
content=("hi this is pinky's file")
with open(filename,"w") as file:
    file.write(content)
with open(filename,"r") as file:
    content2=file.read()
    print(content2)
# we can change the directory,rename...so many functions available

#os.chdir("desktop")
#os.remove()

with open("pinky.txt","a") as file: #append
    file.write(" hello pinky")
with open("tara.txt","a") as file: #append  #keep's appending until we run
    file.write(" hello tara")