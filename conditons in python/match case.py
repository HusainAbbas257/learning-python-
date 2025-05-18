# when checking for multiple values of a single variable we can use match case instead of a if elif ladder
# for example:
number=int(input('enter a number:'))

if(number==1):
    print("one")
elif(number==2):
    print("two")
elif(number==3):
    print("three")
else:
    print("idk?")

# with math case it can be written as :
number=int(input('enter a number:'))
match number:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _: #when no case matches then this case will execute
        print("idk?")
