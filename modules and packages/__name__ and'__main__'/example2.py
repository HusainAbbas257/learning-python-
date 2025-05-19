def greet():
    print("hi from greet()")


print(__name__)
# name contains the name of location from where it is runned 
# it returns __main__ when runned directly else it will return name of calling location
# we can use this to do cool stuff such as
if(__name__!='__main__'):
    print("hey you trying to import my secret file nahh u shudnt do it!!")
else:
    greet()