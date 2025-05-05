class calculate:
    num1=0.0
    num2=0.0
    operation="+"
    def __init__(self,num1=0.0,operation="+",num2=0.0):
        self.num1=num1
        self.num2=num2
        self.operation=operation
        
    def answer(self):
        if(self.operation=="+"):
            self.add() 
        elif(self.operation=="-"):
            self.subtract()
        elif(self.operation=="*"):
            self.multiply()
        elif(self.operation=="/"):
            self.divide()
        elif(self.operation=="^"):
            self.power()
        else:
            print("not a valid operator")
            self.operation="+"
        
    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        print(self.num1-self.num2)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        print(self.num1/self.num2)
    def power(self):
        print(self.num1**self.num2)
    
print(f"----------instruction-----------\n 1.first enter the first number then aperation and then enter second number \n 2.enter + to add,- to subtract,* to multiply,/ to divide,^ to power \n seprate each word by a space \n enter q to exit:")
equation=""
while True:
    equation=input("\n now please enter the equation--->")
    lst=equation.split()
    if(equation=="q"):
        print("thankyou have a nice day!")
        break
    
    calc=calculate(float(lst[0]),lst[1],float(lst[2]))
    print("the answer is:")
    calc.answer()


# -------------------------------------------sample-output-------------------------------------------#
# ----------instruction-----------
#  1.first enter the first number then aperation and then enter second number
#  2.enter + to add,- to subtract,* to multiply,/ to divide,^ to power
#  seprate each word by a space
#  enter q to exit:

#  now please enter the equation--->999.999 + 9000.001 
# the answer is:
# 10000.0

#  now please enter the equation--->17 - -70
# the answer is:
# 87.0

#  now please enter the equation--->-12 * -50
# the answer is:
# 600.0

#  now please enter the equation--->21.8 / 6.8
# the answer is:
# 3.2058823529411766

#  now please enter the equation--->5 ^ 5
# the answer is:
# 3125.0

#  now please enter the equation--->2560000 ^ 0.25
# the answer is:
# 40.0

#  now please enter the equation--->q
# thankyou have a nice day!