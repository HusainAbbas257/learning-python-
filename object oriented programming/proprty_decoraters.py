class Employee:
    # Class variable
    company_name = "Tech Innovators"

    # Class method: works with the class, not the instance
    @classmethod
    def show_company(cls):
        print("Company Name:", cls.company_name)

    def __init__(self, name, salary):
        self._name = name      # Private attribute (by convention)
        self.salary = salary

    # Getter method: allows us to access _name like an attribute
    @property
    def name(self):
        return self._name

    # Setter method: allows us to set _name like an attribute
    @name.setter
    def name(self, value):
        self._name = value

    # Operator overloading: add salaries of two employees
    def __add__(self, other):
        return self.salary + other.salary

    # Operator overloading: subtract salaries
    def __sub__(self, other):
        return self.salary - other.salary

    # Operator overloading: multiply salaries
    def __mul__(self, other):
        return self.salary * other.salary

    # Operator overloading: divide salaries
    def __truediv__(self, other):
        return self.salary / other.salary

    # Floor division
    def __floordiv__(self, other):
        return self.salary // other.salary

    # String method: defines what str(e) prints
    def __str__(self):
        return f"Employee Name: {self._name}, Salary: {self.salary}"

    # Length method: let's say length is the number of characters in the name
    def __len__(self):
        return len(self._name)


# --- USAGE EXAMPLES BELOW ---

# Create Employee objects
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 30000)

# Using class method
Employee.show_company()

# Using property (getter)
print("Employee 1 Name:", e1.name)  # internally calls e1.name()

# Using setter
e1.name = "Alicia"
print("Updated Name:", e1.name)

# Operator overloading
print("Total Salary (e1 + e2):", e1 + e2)          # __add__
print("Salary Difference (e1 - e2):", e1 - e2)     # __sub__
print("Salary Multiply (e1 * e2):", e1 * e2)       # __mul__
print("Salary Division (e1 / e2):", e1 / e2)       # __truediv__
print("Floor Division (e1 // e2):", e1 // e2)      # __floordiv__

# Using __str__ method
print(str(e1))   # or just: print(e1)

# Using __len__ method
print("Length of Employee Name:", len(e1))




#------------------------------------output------------------------------------#
# Company Name: Tech Innovators
# Employee 1 Name: Alice
# Updated Name: Alicia
# Total Salary (e1 + e2): 80000
# Salary Difference (e1 - e2): 20000
# Salary Multiply (e1 * e2): 1500000000
# Salary Division (e1 / e2): 1.6666666666666667
# Floor Division (e1 // e2): 1
# Employee Name: Alicia, Salary: 50000
# Length of Employee Name: 6