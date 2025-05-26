import timeit

# -----------------------------------------------
# FULL EXPLANATION OF timeit MODULE IN 1 SCRIPT
# -----------------------------------------------


print("\n>>> Summary of timeit module:")
print(timeit.__doc__)  # Prints the module docstring

# -------------------------------
# 1. timeit.timeit()
# -------------------------------
# Measures execution time of a code snippet repeated many times
# stmt = code to run; setup = code to run once before; number = repetitions

print("\n>>> timeit.timeit()")
print(timeit.timeit.__doc__)

stmt1 = """
for i in range(100):
    x = i * 2
"""

stmt2 = """
x = [i * 2 for i in range(100)]
"""

# Running both statements 10000 times
time_for_loop = timeit.timeit(stmt=stmt1, number=10000)
time_list_comp = timeit.timeit(stmt=stmt2, number=10000)

print("Time for for-loop:", time_for_loop)
print("Time for list comprehension:", time_list_comp)

# -------------------------------
# 2. timeit.repeat()
# -------------------------------
# Repeats the timeit multiple times and returns a list of results

print("\n>>> timeit.repeat()")
print(timeit.repeat.__doc__)

repeats = timeit.repeat(stmt=stmt1, number=10000, repeat=5)
print("Repeat results (for loop):", repeats)
print("Best time from repeats:", min(repeats))

# -------------------------------
# 3. timeit.default_timer()
# -------------------------------
# Best clock available on the system (perf_counter on most)

print("\n>>> timeit.default_timer()")
print(timeit.default_timer.__doc__)

start = timeit.default_timer()
total = sum(i for i in range(100000))
end = timeit.default_timer()
print("Manual timing using default_timer:", end - start)

# -------------------------------
# 4. timeit.Timer class
# -------------------------------
# Advanced control using class-style approach

print("\n>>> timeit.Timer class")
print(timeit.Timer.__doc__)

setup_code = "from math import sqrt"
stmt_code = "sqrt(12345)"

timer = timeit.Timer(stmt=stmt_code, setup=setup_code)
print("Using Timer class - single run (10000 times):", timer.timeit(10000))
print("Using Timer class - repeat 5 times:", timer.repeat(repeat=5, number=10000))


# Use timeit when:
# - Comparing different methods (e.g., loops vs list comp)
# - Measuring performance of math ops, algorithms, or functions
# - Detecting performance regression
# - Benchmarking small code blocks with accuracy

