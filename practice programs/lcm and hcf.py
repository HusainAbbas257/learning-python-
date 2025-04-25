num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
lcm=num1*num2
hcf=1
smaller =0
if(num1>num2):
    smaller=num2
    bigger=num1
else:
    smaller=num1
    bigger=num2
for i in range(bigger,num1*num2):
    if(i%num1==0 and i%num2==0):
        lcm=i
        break
print("lcm of numbes are:",lcm)



for i in range(smaller,1,-1):
    if(num1%i==0 and num2%i==0):
        hcf=i
        break
print("hcf of numbers are:",hcf)

#sample output:
# enter first number:24
# enter second number:36
# lcm of numbes are: 72
# hcf of numbers are: 12

