# -------------------------------
# 🚀 Data Types and Basic Concepts
# -------------------------------

a = 10              # Assigning an integer value 10 to variable 'a'
print(a)            # Printing the value of 'a'

b = 4.4             # Assigning a float value 4.4 to variable 'b'
print(b)            # Printing the value of 'b'

c = a + b           # Adding 'a' and 'b' and storing the result in 'c'
print(c)            # Printing the result of the addition

s1 = "hello"        # Assigning a string "hello" to variable 's1'
s2 = " world!"      # Assigning a string " world!" to variable 's2'
print(s1 + s2)      # Concatenating and printing the strings 's1' and 's2'

b = False           # Assigning the boolean value False to variable 'b'
print(b)            # Printing the boolean value of 'b'

n = None            # Assigning the special value None (meaning no value) to variable 'n'
print(n)            # Printing the value of 'n'

print(type(n))      # Printing the data type of 'n' (which is <class 'NoneType'>)

# -------------------------------
# ⚙️ Operators and Operands
# -------------------------------

# Arithmetic Operators
x = 15
y = 4

print(x + y)    # Addition: 19
print(x - y)    # Subtraction: 11
print(x * y)    # Multiplication: 60
print(x / y)    # Division: 3.75
print(x // y)   # Floor Division: 3
print(x % y)    # Modulus: 3
print(x ** y)   # Exponentiation: 15^4 = 50625

# Comparison Operators
print(x > y)    # Greater than: True
print(x < y)    # Less than: False
print(x == y)   # Equal to: False
print(x != y)   # Not equal to: True
print(x >= y)   # Greater than or equal to: True
print(x <= y)   # Less than or equal to: False

# Logical Operators with Truth Table
a = True
b = False

# Truth Table for Logical AND
# A       B       A and B
# True    True    True
# True    False   False
# False   True    False
# False   False   False
print(a and b)  # False

# Truth Table for Logical OR
# A       B       A or B
# True    True    True
# True    False   True
# False   True    True
# False   False   False
print(a or b)   # True

# Truth Table for Logical NOT
# A       not A
# True    False
# False   True
print(not a)    # False

# Assignment Operators
z = 10
z += 5          # z = z + 5 → z = 15
print(z)

z *= 2          # z = z * 2 → z = 30
print(z)

z -= 10         # z = z - 10 → z = 20
print(z)

z /= 4          # z = z / 4 → z = 5.0
print(z)

z %= 3          # z = z % 3 → z = 2.0
print(z)

# Bitwise Operators with Truth Table
p = 5           # Binary: 0101
q = 3           # Binary: 0011

# Truth Table for Bitwise AND (&)
# A   B   A & B
# 0   0     0
# 0   1     0
# 1   0     0
# 1   1     1

# Truth Table for Bitwise OR (|)
# A   B   A | B
# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     1

# Truth Table for Bitwise XOR (^)
# A   B   A ^ B
# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     0

print(p & q)    # Bitwise AND: 1 (0001)
print(p | q)    # Bitwise OR: 7 (0111)
print(p ^ q)    # Bitwise XOR: 6 (0110)
print(~p)       # Bitwise NOT: -6 (Inverts all bits, 2's complement)
print(p << 1)   # Left shift: 10 (1010) = 5 * 2
print(p >> 1)   # Right shift: 2 (0010) = 5 // 2

# -------------------------------
# 🔄 Typecasting
# -------------------------------

# Converting int to float
a = 5
print(float(a))     # Output: 5.0

# Converting float to int
b = 6.9
print(int(b))       # Output: 6 (decimal part is truncated)

# Converting int to string
x = 10
print(str(x))       # Output: '10'

# Converting string to int
s = "123"
print(int(s))       # Output: 123

# Converting string to float
f = "3.14"
print(float(f))     # Output: 3.14

# Converting boolean to int
print(int(True))    # Output: 1
print(int(False))   # Output: 0

# Converting int to boolean
print(bool(0))      # Output: False
print(bool(5))      # Output: True