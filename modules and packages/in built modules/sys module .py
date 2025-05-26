import sys

# ------------------------------
# Summary of sys module
# ------------------------------
print("\n>>> Summary of sys module:")
print(sys.__doc__)

# ------------------------------
# 1. sys.version
# ------------------------------
print("\n>>> sys.version")
print(sys.version.__doc__)
print("Python version:", sys.version)

# ------------------------------
# 2. sys.platform
# ------------------------------
print("\n>>> sys.platform")
print(sys.platform.__doc__)
print("Current platform:", sys.platform)

# ------------------------------
# 3. sys.argv
# ------------------------------
print("\n>>> sys.argv")
print(sys.argv.__doc__)
print("List of command-line arguments:", sys.argv)

# ------------------------------
# 4. sys.path
# ------------------------------
print("\n>>> sys.path")
print(sys.path.__doc__)
print("Module search paths:")
for p in sys.path:
    print(p)

# ------------------------------
# 5. sys.modules
# ------------------------------
print("\n>>> sys.modules")
print(sys.modules.__doc__)
print("Total modules currently loaded:", len(sys.modules))

# ------------------------------
# 6. sys.getrecursionlimit()
# ------------------------------
print("\n>>> sys.getrecursionlimit()")
print(sys.getrecursionlimit.__doc__)
print("Current recursion limit:", sys.getrecursionlimit())

# ------------------------------
# 7. sys.setrecursionlimit()
# ------------------------------
print("\n>>> sys.setrecursionlimit()")
print(sys.setrecursionlimit.__doc__)
sys.setrecursionlimit(2000)
print("New recursion limit:", sys.getrecursionlimit())

# ------------------------------
# 8. sys.exit()
# ------------------------------
print("\n>>> sys.exit")
print(sys.exit.__doc__)
print("Use sys.exit() to exit from Python program (not called here)")

# ------------------------------
# 9. sys.stdin, sys.stdout, sys.stderr
# ------------------------------
print("\n>>> sys.stdin, sys.stdout, sys.stderr")
print(sys.stdin.__doc__)
print(sys.stdout.__doc__)
print(sys.stderr.__doc__)
print("Standard input:", sys.stdin)
print("Standard output:", sys.stdout)
print("Standard error:", sys.stderr)

# ------------------------------
# 10. sys.getsizeof()
# ------------------------------
print("\n>>> sys.getsizeof")
print(sys.getsizeof.__doc__)
obj = [1, 2, 3, 4, 5]
print(f"Size of object {obj}: {sys.getsizeof(obj)} bytes")
