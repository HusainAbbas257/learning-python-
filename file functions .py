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

