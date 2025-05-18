#files can be accessed by python too
# first we have to create an object of file to access it by using open(filename,eperation) function as second argument enter "r" to read only
fn="test.txt"
f=open(fn,"r")
# to read the file we can use read() function
s=f.read()
print(s)
f.close()#always close at the end

# to write do open() function again but with "w" as operatio to write
fn="test.txt"
f=open(fn,"w")
# to write  a massege enter it by write() functions
s="this is the new code to be written in the test.txt"
f.write(s)
f.close
# now check agin by readig the file
fn="test.txt"
f=open(fn,"r")
s=f.read()
print(s)
f.close()

#  next function is readlines() it returns a list consisting of each line of file from which it reads
fn="helloworld.py"
f=open(fn,"r")
l=f.readlines()
print(l)
# this list can be combined to a single string as
s=""
for i in l:
    s=s+i
    
print(s)
f.close()

# next function is readline() it print lines of the text untill its ended it returns "" an empty string
fn="helloworld.py"
f=open(fn,"r")
l1=f.readline()
print(l1)
l2=f.readline()
print(l2)
f.close()
# something can be appended in the end of the file in append mode
fn="test.txt"
f=open("test.txt","a")#a means append
f.write("hey this is appended.")
f.close()

# with the above codes you can feel thew butrden of open and close .it has an alternative:with as statements
fl=open("test.txt")
print(fl.read())
fl.close()

with open("test.txt") as fl:
    print(fl.read())

# to just read from a perticular byte of the file we use seek() method 

with open("helloworld.py",'r') as f:
    f.seek(7)#starts reading from 7 th byte
    print(f.read())# prints -->hello world")

# to print only specific number of bytes we give the number of bytes as argument to read()
with open("helloworld.py",'r') as f:
    f.seek(7)#starts reading from 7 th byte
    print(f.read(11))# prints -->hello world

# to get the starting byte we use the tell() function as:
with open("helloworld.py",'r') as f:
    print(f.tell())# by default it has 0 as reading value
    f.seek(7)#starts reading from 7 th byte
    print(f.tell())#gives 7 as starting byte
    
# we can set the file size by using truncate(s) whre s is max size
with open("test.txt",'w') as f:
    f.write("this is the new code to be written in the test.txt")
    f.truncate(10)  #this sets files max size to 10 bytes
with open("test.txt",'r') as f:
    print(f.read())#prints -->this is th

# when you want to reead and write in a same block then u can use multiple open in single with as
with (
    open("helloworld.py",'r') as fr,
    open("test.txt",'w') as fw
):
    fw.write(fr.read())