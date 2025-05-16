n=int(input("enter number of values for which you want to find average:"))
sum=0
for i in range(1,n+1):
    sum+=int(input(f"enter {i}th number:"))
avg=sum/n
print(f"average={avg}")

n=int(input("enter number of values for which you want to find average:"))
sum=0
for i in range(1,n+1):
    sum+=int(input(f"enter {i}th number:"))
avg=sum/n
print(f"average={avg}")


# above code can be written efficiently by using function as:
def average():
    n=int(input("enter number of values for which you want to find average:"))
    sum=0
    for i in range(1,n+1):
        sum+=int(input(f"enter {i}th number:"))
    avg=sum/n
    print(f"average={avg}")
average()
average()

# functions cn be of two types:

# 1.non parametarized --> like above

# 2.parameterized --> it takes parameters 
def average(num1,num2,num3,num4,num5):
    sum=num1+num2+num3+num4+num5
    avg=sum/5
    print(f"average={avg}")

a,b,c,d,e=int(input(f"enter 1st number:")),int(input(f"enter 2nd number:")),int(input(f"enter 3rd number:")),int(input(f"enter 4th number:")),int(input(f"enter 5th number:"))
average(a,b,c,d,e)
a,b,c,d,e=int(input(f"enter 1st number:")),int(input(f"enter 2nd number:")),int(input(f"enter 3rd number:")),int(input(f"enter 4th number:")),int(input(f"enter 5th number:"))
average(a,b,c,d,e)

# function always return a value
# above function's return can be got by:
print(average(1,2,3,4,5)) #returns none

# functions can be made of return type by using return satement.eg
a,b,c,d,e=int(input(f"enter 1st number:")),int(input(f"enter 2nd number:")),int(input(f"enter 3rd number:")),int(input(f"enter 4th number:")),int(input(f"enter 5th number:"))
def average(num1,num2,num3,num4,num5):
    sum=num1+num2+num3+num4+num5
    avg=sum/5
    return avg
print(average(1,2,3,4,5))

# if all arguments are not passed then it might throw an error .To prevent this error arguments are assigned with a default value
a,b,c,d,e=int(input(f"enter 1st number:")),int(input(f"enter 2nd number:")),int(input(f"enter 3rd number:")),int(input(f"enter 4th number:")),int(input(f"enter 5th number:"))
def average(num1=0,num2=0,num3=0,num4=0,num5=0):
    sum=num1+num2+num3+num4+num5
    avg=sum/5
    return avg
print(average(1,2,3,4,5))


# arguments of a function as well as as its return can be given their datatype at the time of declaration as:
a,b,c,d,e=int(input(f"enter 1st number:")),int(input(f"enter 2nd number:")),int(input(f"enter 3rd number:")),int(input(f"enter 4th number:")),int(input(f"enter 5th number:"))
def average(num1:int=0,num2:int=0,num3:int=0,num4:int=0,num5:int=0) ->int:#this will now return the value as an ineteger
    sum=num1+num2+num3+num4+num5
    avg=sum/5
    return avg
print(average(a,b,c,d,e))

#there are many times when a need of function with a variable number arguments is needed for such a case we use * before arguments name toconvert all the entered arguments into a list
# example:
def sum(*args:float)->float:
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(1,2,3,4,5,6,7,8,9,10))

# we use **before arguments name to make it a dictionary input with costum size.example

def set(**kwargs):
     print(kwargs)
     for i in kwargs:
       print(i)
set(one=1,two=2,three=3)