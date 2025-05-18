a="this is declareed outside any class"
class example:
    b="this is declared outide any method but inside the class"
    def func1(self):
        c="this is declared inside func1"
        print("from inside of func1 here is c:",c)
    def func2(self):
        global d
        d="this is declared inside func2"
        # a="a got changed" this will not change a instead it will creat a new local variable with name a
        # b="b got changed" this will not change b instead it will creat a new local variable with name b
        # c="c got changed" this will not change c instead it will creat a new local variable with name c
        d="d got changed inside func2"   

d="d outside class"
print(a) #a is declared outside any class so it can only be accesed only outside the classes
# print(b) it will cause an error as b can be used in its class only
ex= example()
print(ex.b)
# print(ex.c)   c can only be accessed inside of func1 but d is declared with global keyword so it can be accessed without calling change()
print(d) #d can be accessed here however its default value gets executed
ex.func2()
print(d)    #now d can be called any where and used the func2 method to change its value

# ----------------------------------output ----------------------------------#
# this is declareed outside any class
# this is declared outide any method but inside the class
# d outside class
# d got changed inside func2
