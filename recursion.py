# when a number is called inside itself then it is defined in its own terms this is called recursion


# A simple recursive function to calculate factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial Program Using Recursion")
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)
