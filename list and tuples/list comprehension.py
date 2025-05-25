# when  we want to have a list with some costum values we can use loops as:
# if we need a list of all perfect squares between 0 to 100
l1:list=[]
for i in range(11):
    l1.append(i*i)
print(l1)

# we can use inline loop or list comprehension to simplify this task as:
l2=[i*i for i in range(11)]
# this will store all i square valueas from 0 to 10 for i
print(l2)

# if we ever needed to copy some elements of but with some condiitons we can also use if in it as:
l3=[i for i in l2 if i%2==0]  #this will store all even perfect squares from l2
print(l3)