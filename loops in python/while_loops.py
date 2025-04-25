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
#while loops execute the the statements in them untill the condition in them turns false
num=1
while(num<=11):
    print(num)
    num+=1

#example 2:
n =int(input("enter a number to get its table:"))
i=1
while(i<=10):
    print(i*n)
    i+=1

# if the condition in the while is always true then it becomes an infinite loop.for example:
# i=1
# while(i>=1):
#     print(i)
#     i+=1


#while can be used to iterate over lists for examples:
list=[9,8,7,6,5,4,3,2,1,0]
i=0
while(i<len(list)):
    print(list[i])
    i+=1

#while can be used to iterate over tuples for examples:
my_tuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

#while can be used to iterate over strings for examples:
my_string = "hello"
i = 0
while i < len(my_string):
    print(my_string[i])
    i += 1
