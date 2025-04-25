#control statements move the control to a specefic point in the program they are perticularly used with loops
#1.break statement:quickly moves control out of the loop and starts executing from there
for  i in range(20):
    if(i==15):
      break  #it will only execute when i==15
    print("inside the loop:",i)
print("outside the loop")
#this prints all the number from 1 to 20 hundred but breaks the loop at 15 .output:
# inside the loop: 0
# inside the loop: 1
# inside the loop: 2
# inside the loop: 3
# inside the loop: 4
# inside the loop: 5
# inside the loop: 6
# inside the loop: 7
# inside the loop: 8
# inside the loop: 9
# inside the loop: 10
# inside the loop: 11
# inside the loop: 12
# inside the loop: 13
# inside the loop: 14
# outside the loop

#another example:this will print only a single word of the string
s="python is cool"
for i in s:
    if(i==' '):
      break
    print(i)

# output: 
# p
# y
# t
# h
# o
# n


#2.continue ->skips this perticular iteration from that point and transfers the loop to second iteration

i=0
for  i in range(20):
    if(i==15):
      continue  #it will only execute when i==15
    print("inside the loop:",i)
print("outside the loop")

#this loop will run all the way from one to 10 but skips the iteration involving when i==15.output:
# inside the loop: 0
# inside the loop: 1
# inside the loop: 2
# inside the loop: 3
# inside the loop: 4
# inside the loop: 5
# inside the loop: 6
# inside the loop: 7
# inside the loop: 8
# inside the loop: 9
# inside the loop: 10
# inside the loop: 11
# inside the loop: 12
# inside the loop: 13
# inside the loop: 14
# inside the loop: 16
# inside the loop: 17
# inside the loop: 18
# inside the loop: 19
# outside the loop

#another example:this will print every single word of the string but will skip the white spaces
s="python is cool"
for i in s:
    if(i==' '):
      continue
    print(i)

#output;
# p
# y
# t
# h
# o
# n
# i
# s
# c
# o
# o
# l 

#3.pass--> it simply instructs that loop does nothing .for example:
# for i in range(20):

# print("outside the loop ")
# loop is empty so a error will be thrown to avoid it we simply write a pass statement inside the loop.Example:
for i in range(20):
    pass
print("outside the loop" )
#  output:
# outside the loop