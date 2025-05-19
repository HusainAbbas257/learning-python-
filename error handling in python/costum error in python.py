# sometimes we need to raise an error when no pre defined erro for that case exists such as;
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")  # manually raising error by using raise statement
print("Your age is", age)


#  we can also put this all into a try except block for better results
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")  # manually raising error
    print("Your age is", age)
except Exception as e:
    print(f"error occured:{e}")


# well we didnt actualy created an error we just renamed trhe value error
# to create a error we need to create an empty sub class of Exception for example
class PasswordTooShort(Exception):
    pass

try:
    password = input("Enter password: ")
    if len(password) < 6:
        raise PasswordTooShort("Password must be at least 6 characters long.")
except Exception as e:
    print("❌ Error:", e)
else:
    print("Password accepted.")