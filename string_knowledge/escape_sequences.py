# Escape Sequences in Python with Examples

# \n : Newline character
print("Hello\nWorld")  # Output:
# Hello
# World

# \t : Tab space
print("Name:\tJohn")  # Output: Name:    John

# \\ : Backslash
print("This is a backslash: \\")  # Output: This is a backslash: \

# \' : Single quote inside single-quoted string
print('It\'s a sunny day')  # Output: It's a sunny day

# \" : Double quote inside double-quoted string
print("He said, \"Hello\"")  # Output: He said, "Hello"

# \r : Carriage return (moves cursor to the beginning)
print("12345\rAB")  # Output: AB345 (12345 is overwritten from beginning)

# \b : Backspace (removes the character before it)
print("Helloo\b")  # Output: Hello (last 'o' removed)

# \f : Form feed (rarely used)
print("Hello\fWorld")  # Output may vary depending on interpreter

# \a : Bell/alert (may make a sound in some systems)
print("Beep\a")  # Try this in a terminal, might hear a beep

# \v : Vertical tab (also rarely used)
print("Hello\vWorld")  # Output: Hello (newline + indented World)

# \ooo : Octal value
print("\101\102\103")  # Output: ABC (octal for A=101, B=102, C=103)

# \xhh : Hex value
print("\x48\x49")  # Output: HI (hex 48 = H, 49 = I)

# This is a demo of how escape sequences work in Python
# You can try these and see the result in your console

# Note: Some of these may look different in online IDEs or editors
# Always best to try them in a terminal or text-based interface for exact effect
git 