#Numbers from 1 to 10 can be printed like this but on a large scale it tooks a lot of work to do 
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#this effort can be overcomed by using loops
#for loops execute the the statements in them untill the range in them is valid
#for example:
a=1
b=10
c=1
for i in range(a,b,c):      #a=strating point b=ending point c=size of each step
    print(i)

#another example;
n =int(input("enter a number to get its table:"))
for i in range(1,11):     
    print(i*n)


#for can be used to iterate over lists for examples:
l=[9,8,7,6,5,4,3,2,1,0]
for i in l:
    print(i)

#for can be used to iterate over tuples for examples:
my_tuple = ('apple', 'banana', 'cherry')
for item in my_tuple:
    print(item)

#for can be used to iterate over strings for examples:
my_string = "hello"
for char in my_string:
    print(char)

#for loop can also be used with else. Material inside else will be executed when condition of loop is exhausted
for i in range(5):
    print(i)
else:
    print("Loop ended normally.")
