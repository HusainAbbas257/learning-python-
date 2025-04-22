
# ------------------------------------------
# IF / ELIF / ELSE in Python
# ------------------------------------------

# Definition:
# if       - checks a condition, runs block if True
# elif     - checks another condition, only if previous are False
# else     - runs if none of the above are True

# Flow of control: Top to bottom. As soon as one condition is True,
# its block runs and the rest are skipped.

# ------------------------------------------
# Example 1: Using only `if`
print("Example 1: Only IF")
age = 20

if age >= 18:
    print("You are an adult.")  # Runs only if the condition is True

print()  # spacer

# ------------------------------------------
# Example 2: IF + ELSE
print("Example 2: IF + ELSE")
is_raining = False

if is_raining:
    print("Take an umbrella!")
else:
    print("Enjoy the sunshine!")

print()  # spacer

# ------------------------------------------
# Example 3: IF + ELIF + ELSE
print("Example 3: IF + ELIF + ELSE")
temperature = 30  # Change this value to test

if temperature > 35:
    print("It's very hot outside!")
elif temperature > 25:
    print("It's a warm day.")
elif temperature > 15:
    print("It's a bit cold.")
else:
    print("It's really cold!")

print()  # spacer

# ------------------------------------------
# Example 4: Grade Checker
print("Example 4: Grade Checker")
marks = 68  # Try changing the marks

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# ----------------sample output-------------#
# Example 1: Only IF
# You are an adult.

# Example 2: IF + ELSE
# Enjoy the sunshine!

# Example 3: IF + ELIF + ELSE
# It's a warm day.

# Example 4: Grade Checker
# Grade: C