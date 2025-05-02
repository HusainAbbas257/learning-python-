class Employee:
    # a class i a blue print that contains all the informtion of all objects
    # following variables are class variables which remain same for all objects
    company="abcd corporations"
    salary=50000
    def get(obj):#this method takes a obj value which is an object of Employee class and print its attributes
        print(f"company={obj.company},salary={obj.salary}")

# an object can be created be simply calling the class name with () outside the class
adam= Employee()#an object is an entity that contains all the information of class including its owns
adam.name="adam"#this is an instance variable which is maybe different for all objects
print(f"name={adam.name},company={adam.company},salary={adam.salary}")

# a single class can have multiple objects each with a different unique value
boss=Employee()
boss.salary=100000  #when a instance value is available for class variable then it is prioritized over class value
boss.name="xyz sir"
print(f"name={boss.name},company={boss.company},salary={boss.salary}")
Employee.get(boss)
# we can call the method by the object
adam.get()#however no argument wass passed it automatically makes adam as its argument

