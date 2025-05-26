# Importing required libraries
import time                # Used for the timer decorator (to measure execution time)
import functools           # Used to preserve function metadata when using decorators

# ----------------------------------------
# 1. Basic Decorator
# ----------------------------------------

# This is a very simple decorator that wraps another function
def simple_decorator(func):
    # The wrapper function adds behavior before and after the original function
    def wrapper():
        print("Before the function runs")
        func()  # Call the original function
        print("After the function runs")
    return wrapper  # Return the new wrapped function

# Apply the decorator using '@' syntax
@simple_decorator
def greet():
    print("Hello from greet() function!")


print("\n1. Basic Decorator:")
greet()


# ----------------------------------------
# 2. Decorator with Arguments
# ----------------------------------------

# This is a decorator factory (a function that returns a decorator)
# It allows us to pass arguments to the decorator
def repeat(times):
    # The actual decorator that will receive the function
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):  # Repeat 'times' number of times
                func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator  # Return the actual decorator

@repeat(3)  # Repeat the function 3 times
def say_hello(name):
    print(f"Hello, {name}")


print("\n2. Decorator with Arguments:")
say_hello("Kumail")

# ----------------------------------------
# 3. Using functools.wraps to preserve metadata
# ----------------------------------------

# This decorator logs the name of the function being called
def smart_decorator(func):
    @functools.wraps(func)  # Preserves the function name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@smart_decorator
def add(a, b):
    """Returns sum of two numbers"""
    return a + b


print("\n3. With functools.wraps:")
print(f"Result: {add(2, 3)} | Docstring: {add.__doc__}")

# ----------------------------------------
# 4. Chaining Multiple Decorators
# ----------------------------------------

# First decorator adds <b> HTML tags around the result
def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

# Second decorator adds <i> HTML tags
def italic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

# This function is now decorated with both bold and italic
# Note: Closest decorator (italic) runs first
@bold
@italic
def formatted_text():
    return "Hello, world"

print("\n4. Chaining Decorators:")
print(formatted_text())

# ----------------------------------------
# 5. Real-World Example 1: Logging
# ----------------------------------------

# A decorator to log function calls
def log(func):
    @functools.wraps(func)  # Preserve original function metadata
    def wrapper(*args, **kwargs):
        print(f"LOG: {func.__name__} called with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def divide(x, y):
    return x / y

print("\n5. Logging Decorator:")
print(divide(10, 2))


# ----------------------------------------
# 6. Real-World Example 2: Timer
# ----------------------------------------

# A decorator that calculates and prints how long a function takes to run
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()            # Record start time
        result = func(*args, **kwargs) # Call the function
        end = time.time()              # Record end time
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

@timer
def slow_function():
    count=0
    for i in range(1000):
        count=i  # Simulates a slow task by counting to 1000
    return f"Finished counting till {count}"

print("\n6. Timer Decorator:")
print(slow_function())

# ----------------------------------------
# 7. Real-World Example 3: Caching
# ----------------------------------------

# Dictionary to store previously computed values
cache = {}

# This decorator caches results of a function to speed up repeated calls
def cached(func):
    @functools.wraps(func) # preserveeng meta data
    def wrapper(n):
        if n in cache:#already a value exist or not
            print(f"Returning cached result for {n}")
            return cache[n]
        result = func(n)
        cache[n] = result  # Save result in cache
        return result
    return wrapper

@cached
def fib(n):
    # recursive Fibonacci to show use of above
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print("\n8. Caching Decorator:")
print(f"Fibonacci of 10: {fib(10)}")     # Slow for the first time
print(f"Fibonacci of 10 again: {fib(10)}") # Fast due to caching



    

   
    


    

    

    
