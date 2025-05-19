import math

# in this program we will see different functions of math module and their usage

# 1. Square Root and Power
num = float(input("Enter a number to find its square root: "))
print("Square root:", math.sqrt(num))

base = float(input("Enter the base number for exponentiation: "))
exponent = float(input("Enter the exponent: "))
print("Result of power:", math.pow(base, exponent))

# 2. Trigonometric Functions
angle_deg = float(input("Enter an angle in degrees to find its sine: "))
angle_rad = math.radians(angle_deg)
print("Sine of angle:", math.sin(angle_rad))

# 3. Angle Conversion
deg = float(input("Enter angle in degrees to convert to radians: "))
print("Radians:", math.radians(deg))

rad = float(input("Enter angle in radians to convert to degrees: "))
print("Degrees:", math.degrees(rad))

# 4. Floor, Ceil and Truncate
decimal_num = float(input("Enter a decimal number for floor, ceil and truncate: "))
print("Floor value:", math.floor(decimal_num))
print("Ceil value:", math.ceil(decimal_num))
print("Truncated value:", math.trunc(decimal_num))

# 5. Absolute and Sign
negative_num = float(input("Enter any negative number to get its absolute value: "))
print("Absolute value:", math.fabs(negative_num))

sign_base = float(input("Enter a number (whose magnitude will be taken): "))
sign_ref = float(input("Enter another number (whose sign will be copied): "))
print("Copy sign result:", math.copysign(sign_base, sign_ref))

# 6. Logarithmic Functions
log_num = float(input("Enter a number to find its log base 10: "))
print("Log base 10:", math.log10(log_num))
print("Log base 2:", math.log2(log_num))
base_log = float(input("Enter a number for log base N: "))
log_base = float(input("Enter the base: "))
print("Log base N:", math.log(base_log, log_base))

# 7. GCD and LCM
a = int(input("Enter first integer for GCD and LCM: "))
b = int(input("Enter second integer: "))
print("GCD:", math.gcd(a, b))
print("LCM:", math.lcm(a, b))

# 8. Factorial, Combinations and Permutations
fact_num = int(input("Enter a number to find its factorial: "))
print("Factorial:", math.factorial(fact_num))

n = int(input("Enter n for combinations (nCr): "))
r = int(input("Enter r for combinations (nCr): "))
print("Combinations (nCr):", math.comb(n, r))
print("Permutations (nPr):", math.perm(n, r))

# 9. Hypotenuse
x = float(input("Enter side 1 of right triangle: "))
y = float(input("Enter side 2: "))
print("Hypotenuse:", math.hypot(x, y))

# 10. Remainder and modf
dividend = float(input("Enter a number to get remainder when divided by 3: "))
print("Remainder (closest to 0):", math.remainder(dividend, 3))

modf_num = float(input("Enter a decimal number to split into fraction and integer parts: "))
fractional, integer = math.modf(modf_num)
print("Fractional part:", fractional)
print("Integer part:", integer)

# 11. Special values and checks
check_num = float(input("Enter two numbers to check if they are close: \nFirst number: "))
check_num2 = float(input("Second number: "))
print("Are they close?", math.isclose(check_num, check_num2))

print("Is math.inf finite?", math.isfinite(math.inf))
print("Value of pi:", math.pi)
print("Value of e:", math.e)
print("Infinity representation:", math.inf)
print("NaN representation:", math.nan)




#------------------sample-output---------------#
# Enter a number to find its square root: 1024
# Square root: 32.0
# Enter the base number for exponentiation: 2
# Enter the exponent: 10
# Result of power: 1024.0
# Enter an angle in degrees to find its sine: 45
# Sine of angle: 0.7071067811865476
# Enter angle in degrees to convert to radians: 90
# Radians: 1.5707963267948966
# Enter angle in radians to convert to degrees: 3.14
# Degrees: 179.9087476710785
# Enter a decimal number for floor, ceil and truncate: 3.14
# Floor value: 3
# Ceil value: 4
# Truncated value: 3
# Enter any negative number to get its absolute value: -100
# Absolute value: 100.0
# Enter a number (whose magnitude will be taken): 5
# Enter another number (whose sign will be copied): -6
# Copy sign result: -5.0
# Enter a number to find its log base 10: 100
# Log base 10: 2.0
# Log base 2: 6.643856189774724
# Enter a number for log base N: 81
# Enter the base: 3
# Log base N: 4.0
# Enter first integer for GCD and LCM: 36
# Enter second integer: 27
# GCD: 9
# LCM: 108
# Enter a number to find its factorial: 5
# Factorial: 120
# Enter n for combinations (nCr): 5
# Enter r for combinations (nCr): 4
# Combinations (nCr): 5
# Permutations (nPr): 120
# Enter side 1 of right triangle: 3
# Enter side 2: 4
# Hypotenuse: 5.0
# Enter a number to get remainder when divided by 3: 100
# Remainder (closest to 0): 1.0
# Enter a decimal number to split into fraction and integer parts: 3.14
# Fractional part: 0.14000000000000012
# Integer part: 3.0
# Enter two numbers to check if they are close:
# First number: 19
# Second number: 20
# Are they close? False
# Is math.inf finite? False
# Value of pi: 3.141592653589793
# Value of e: 2.718281828459045
# Infinity representation: inf
# NaN representation: nan