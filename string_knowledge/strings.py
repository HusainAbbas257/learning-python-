# Program to demonstrate string slicing and skipping characters in Python

# Get user input
s = input("Enter a string: ")
length = len(s)  # Calculate the length of the string
print("Length of the string:", length)

# Ask the user for the starting and ending positions for slicing
a = int(input("Select the starting position (index): "))
b = int(input("Select the ending position (index, non-inclusive): "))

# Slice the string from position 'a' to 'b'
# Note: Python uses 0-based indexing and excludes the character at index 'b'
new_s = s[a:b]

print("Sliced string (without skipping):", new_s)

# Now demonstrate skipping characters using slicing
# Ask the user how many characters to skip
skip = int(input("Now enter a skip value (e.g., 1 for every character, 2 for every second character, etc.): "))

# Apply slicing with skipping
new_s_skipped = s[a:b:skip]
print("Sliced string (with skipping):", new_s_skipped)



# ------------------ Sample Output ------------------
# Example 1:
# Enter a string: neil armstrong
# Length of the string: 14
# Select the starting position (index): 8
# Select the ending position (index, non-inclusive): 14
# Sliced string (without skipping): strong
# Now enter a skip value: 2
# Sliced string (with skipping): sron

# ---------------------------------------------------
# More Examples:
# s = "abcdefghijk"
#len(s)          ->11 
# s[2:8]         -> 'cdefgh'
# s[2:8:2]       -> 'ceg'
# s[:]           -> full string copy
# s[::2]         -> every second character from the whole string
# s[::-1]        -> reverses the string
