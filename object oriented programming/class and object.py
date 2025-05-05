class Employee:
    # a class i a blue print that contains all the informtion of all objects
    # following variables are class variables which remain same for all objects
    company="abcd corporations"
    salary=50000
    def get(self):#this method takes a self value which is an object of Employee class and print its attributes
        print(f"name={self.name},company={self.company},salary={self.salary}")#this types of methodes are called self methods 

    @staticmethod
    def sayhi():
        print("hi!")
    
    def __init__(self,name="",company="abcd corporations",salary=50000):
        self.name=name
        self.company=company
        self.salary=salary
# an object can be created be simply calling the class name with () outside the class
adam= Employee()#an object is an entity that contains all the information of class including its owns
adam.name="adam"#this is an instance variable which is maybe different for all objects
print(f"name={adam.name},company={adam.company},salary={adam.salary}")

# a single class can have multiple objects each with a different unique value=
boss=Employee()
boss.salary=100000  #when a instance value is available for class variable then it is prioritized over class value
boss.name="xyz sir"
print(f"name={boss.name},company={boss.company},salary={boss.salary}")
Employee.get(boss)
# we can call the method by the object
adam.get()#however no argument wass passed it automatically makes adam as its argument

# sayhi method doesnot require any object but it gets defaulty passed to it creating an error
#  to prevent it we use @staticmethod before defining the function
boss.sayhi()#now it will not cause an error

# there is always a need of something to prevent initialization of all values one by one
# and that game changer is __init__ function aka constuctor
# it is a special function that gets automaticaly called at the time of object creation
newemp=Employee("mr. cleaner","xyz company",5000)
newemp.get()