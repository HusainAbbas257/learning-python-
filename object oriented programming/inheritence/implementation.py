# Base class
class Polygon:
    def __init__(self, sides=[], angles=[], area=0, perimeter=0):
        self.sides = sides
        self.angles = angles
        self.area = area
        self.perimeter = perimeter

    def calculate_perimeter(self):
        self.perimeter = sum(self.sides)

    def display(self):
        print(f"Sides: {self.sides}")
        print(f"Angles: {self.angles}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter} \n")

# ------------------- Branch 1: Quadrilateral Family -------------------

class Quadrilateral(Polygon):
    def __init__(self, sides=[], angles=[]):
        super().__init__(sides, angles)

class Parallelogram(Quadrilateral):
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height
        sides = [base, side, base, side]
        angles = [90, 90, 90, 90]  # generalized as right angles for simplicity
        super().__init__(sides, angles)
        self.calculate_area()
        self.calculate_perimeter()

    def calculate_area(self):
        self.area = self.base * self.height

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.base + self.side)

class Rectangle(Parallelogram):
    def __init__(self, length, breadth):
        super().__init__(length, breadth, breadth)  # height = breadth for area
        self.angles = [90, 90, 90, 90]
    
class Rhombus(Parallelogram):
    def __init__(self, side=0, height=0,angles=[]):
        super().__init__(side, side, height)
        self.angles = angles # common rhombus angles

# Multiple Inheritance: Square is both a Rectangle and Rhombus
class Square(Rectangle, Rhombus):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        Rhombus.__init__(self,side,side,)
        self.angles = [90, 90, 90, 90]

# ------------------- Branch 2: Triangle Family -------------------

class Triangle(Polygon):
    def __init__(self, a, b, c):
        sides = [a, b, c]
        perimeter = a + b + c
        s = perimeter / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        angles = []  # angles unknown
        super().__init__(sides, angles, area, perimeter)

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.angles = [60, 60, 60]

# ------------------- Object Creation & Testing -------------------

print("=== Square ===")
sq = Square(5)
sq.display()

print("\n=== Rectangle ===")
rect = Rectangle(4, 6)
rect.display()

print("\n=== Rhombus ===")
rhom = Rhombus(4, 3)
rhom.display()

print("\n=== Parallelogram ===")
para = Parallelogram(6, 4, 5)
para.display()

print("\n=== Triangle ===")
tri = Triangle(3, 4, 5)
tri.display()

print("\n=== Equilateral Triangle ===")
eq_tri = EquilateralTriangle(6)
eq_tri.display()


#-----------------------output-----------------------#
# === Square ===
# Sides: [5, 5, 5, 5]
# Angles: [90, 90, 90, 90]
# Area: 25
# Perimeter: 20 


# === Rectangle ===
# Sides: [4, 6, 4, 6]
# Angles: [90, 90, 90, 90]
# Area: 24
# Perimeter: 20 


# === Rhombus ===
# Sides: [4, 4, 4, 4]
# Angles: []
# Area: 12
# Perimeter: 16 


# === Parallelogram ===
# Sides: [6, 4, 6, 4]
# Angles: [90, 90, 90, 90]
# Area: 30
# Perimeter: 20 


# === Triangle ===
# Sides: [3, 4, 5]
# Angles: []
# Area: 6.0
# Perimeter: 12 


# === Equilateral Triangle ===
# Sides: [6, 6, 6]
# Angles: [60, 60, 60]
# Area: 15.588457268119896
# Perimeter: 18 

