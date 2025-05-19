# Handling Different Runtime Errors with try-except

# Example without error handling
num1 = int(input("Enter a number for division: "))
num2 = int(input("Enter another number for division: "))

answer = num1 / num2
print("Answer =", answer)

# Above code will break if:
# - You divide by 0 ➜ ZeroDivisionError
# - You enter something that's not a number ➜ ValueError

# So now let's handle errors properly!

# ✅ Basic try-except for ZeroDivisionError
num1 = int(input("Enter a number for division: "))
num2 = int(input("Enter another number for division: "))

try:
    answer = num1 / num2
    print("Answer =", answer)
except ZeroDivisionError:
    print("Looks like you are trying to divide by zero!")


# ✅ Multiple except blocks for different types of runtime errors
try:
    num1 = int(input("Enter a number for division: "))  # Might raise ValueError
    num2 = int(input("Enter another number for division: "))  # Might raise ValueError
    answer = num1 / num2  # Might raise ZeroDivisionError
    print("Answer =", answer)

except ZeroDivisionError:
    print("❌ Error: You cannot divide by zero!")

except ValueError:
    print("❌ Error: Input must be a number!")

except Exception as e:
    print(f"❌ Unexpected Error: {e}")  # Catch-all for any other error


# ✅ Example: Handling IndexError
try:
    my_list = [10, 20, 30]
    print(my_list[5])  # Index doesn't exist
except IndexError:
    print("❌ Error: List index out of range!")


# ✅ Example: Handling FileNotFoundError
try:
    with open("non_existing_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("❌ Error: File not found!")


# ✅ Example: Handling TypeError
try:
    result = "string" + 5  # Can't add str and int
except TypeError:
    print("❌ Error: Cannot add string and integer!")


# ✅ Example: Handling NameError
try:
    print(undefined_variable)  # variable not declared
except NameError:
    print("❌ Error: Variable not defined!")


# ✅ Example: Handling KeyError
try:
    d = {"name": "Ali"}
    print(d["age"])
except KeyError:
    print("❌ Error: Key not found in dictionary!")


# ✅ Example: Handling AttributeError
try:
    x = 10
    x.append(5)  # int has no append
except AttributeError:
    print("❌ Error: Object does not support this attribute!")

# WHEN ITS NOT CLEAR WHICH TYPE OF ERROR WILL BE THROWN WE CAN USE EXCETTION ERROR IT IS LIKE PARENT OF EVERY ERROR AND GET IT AS AN OBJECT AS:
try:
    print("i hate errors"+100)
except Exception as e:
    print(e) #this prints details of error-->can only concatenate str (not "int") to str


# TO EXECUTE A BLOCK WHEN THE CODE RUNS WITHOUT ANY ERROR WE USE ELSE AFTER EXCEPT .for example
try:
    num=int(input("enter a number to get its square:"))
except Exception as e:
    print("an error occured:",e)
else:
    print("no error occured.answer=",(num*num))

# if you want to make sure a specific block must execute always no matter an error occurs or not
try:
    num=int(input("enter a number to get its square:"))
except Exception as e:
    print("an error occured:",e)
else:
    print("no error occured.answer=",(num*num))
finally:
    print("this will always execute")