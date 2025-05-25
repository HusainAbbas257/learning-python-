from functools import reduce

# map, filter, and reduce are built-in functions in Python for functional-style operations on iterables.
# They help avoid traditional loops, making your code concise and powerful.

# Let's see the built-in docstrings:
print("\nmap docstring:\n", map.__doc__)
print("\nfilter docstring:\n", filter.__doc__)
print("\nreduce docstring:\n", reduce.__doc__)

# Sample list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. map(function, iterable)
# Applies a function to every item in the iterable

def square(n: int) -> int:
    return n * n

# Traditional approach
print("\nSquares using loop:")
for l in lst:
    print(square(l), end=' ')

# Using map
print("\n\nSquares using map:")
mapped = map(square, lst)
print(list(mapped))

# 2. filter(function, iterable)
# Filters out elements for which the function returns False

def is_even(n: int) -> bool:
    return n % 2 == 0

# Traditional approach
print("\nEven numbers using loop:")
for l in lst:
    if is_even(l):
        print(l, end=' ')

# Using filter
print("\n\nEven numbers using filter:")
filtered = filter(is_even, lst)
print(list(filtered))

# 3. reduce(function, iterable)
# Applies a rolling computation to sequential pairs from the iterable

def product(x: int, y: int) -> int:
    return x * y

# Traditional approach to multiply all elements
print("\nProduct using loop:")
result = 1
for l in lst:
    result *= l
print(result)

# Using reduce
print("\nProduct using reduce:")
reduced = reduce(product, lst)
print(reduced)
