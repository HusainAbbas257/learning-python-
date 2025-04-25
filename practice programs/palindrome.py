s=input("enter a string for palindrome check:")
palin=""
for ch in s:
    palin=ch+palin
if(palin==s):
    print("it is palindrome")
else:
    print("it is not palindrome")
