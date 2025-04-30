num=0.0
s=2
while(num<=s):
    if(num==1 or num==2 or num==3):
        print("y")
    if(round(num**num )==s):
        print("found:",num)
        break
    else:
        num+=0.00000001
print("not found")