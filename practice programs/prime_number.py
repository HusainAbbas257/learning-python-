num=int(input("enter a number for prime check:"))
is_prime=True
for i in range(2,num):
    if(num%i==0):
        is_prime=False
        break
    
if(is_prime==True):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")