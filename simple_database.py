
def signup():
    id=input("enter your id:")
    with open("data/ids.txt") as f:
        if(id in f.read()):
            print("sorry try another user name this is already taken!")
            return "retry"
        else:
            tf=open("data/ids.txt","a")
            tf.write(id+"\n")
    password=input("enter your password:")
    with open("data/passwords.txt","a") as f:
        f.write(password+"\n")
    secret=input("enter your secret:")
    with open("data/secrets.txt","a") as f:
        f.write(secret+"\n")
    return "success"

def find(string,filename):
    for loc in range(1,100):
        with open(filename,"r") as f:
            if(string+"\n"==f.readline()):
                return loc
    else:
        return -1

def stringatline(n,filename):
    with open(filename,"r") as f:
        itemlist=f.readlines()
    return itemlist[n-1]


def login():
    linen=0
    id=input("enter your id:")
    linen=find(id,"data/ids.txt")
    if(linen==-1):
        print("no such id found:")
        return "failed"
    else:
        attempt=0
        password=""
        while((password+"\n")!=stringatline(linen,"data/passwords.txt")):
            password=input("enter your password:")
            attempt+=1
            if(attempt>=5):
                print("too many incorrect tries . try again later!")
                return "failed"
            if((password+"\n")==stringatline(linen,"data/passwords.txt")):
                print("succesfully logged into your account")
                print(f"your secret string is  --->{stringatline(linen,"data/secrets.txt")}")
                return "success"
        
        
    


#this all has to be saved in secret data to keep record-->"data"
# first ask user to login or signup:
choice1=input("do you want to login or signup:")
if(choice1=="signup"):
    signup_status="retry"
    while(signup_status=="retry"):
        signup_status=signup()
        if(signup_status=="success"):
            print("you account has been created succesfully")
            break
elif(choice1=="login"):
    while True:
        if(login()=="success"):
            break
else:
    print("please enter a valid choice")
    


# <--------------------sample-output-------------------->
# PS C:\Users\DELL\Desktop\learning-python-> python .\simple_database.py
# enter your id:fake elon musk
# enter your password:ihatetomato
# enter your secret:i am secretly donating my entire wealth to the person who wrote this amazing code
# you account has been created succesfully
# PS C:\Users\DELL\Desktop\learning-python-> python .\simple_database.py
# do you want to login or signup:signup
# enter your id:husainabbas257
# enter your secret:i want to hack elon musk account to know its secret
# you account has been created succesfully
# PS C:\Users\DELL\Desktop\learning-python-> python .\simple_database.py
# do you want to login or signup:signup
# enter your id:fake elon musk
# sorry try another user name this is already taken!
# enter your id:i dont know
# enter your password:i dont know
# enter your secret:i kow everything and everyones secret
# you account has been created succesfully
# PS C:\Users\DELL\Desktop\learning-python-> python .\simple_database.py        
# do you want to login or signup:login
# enter your id:fake elon musk 
# enter your password:qazwsxedcrftgbyhnujmik,o   
# enter your password:\nnn
# enter your password:\n \n
# enter your password:ihatetomato
# succesfully logged into your account
# your secret string is  --->i am secretly donating my entire wealth to the person who wrote this amazing code