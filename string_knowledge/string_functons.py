s1 = input("Input a string to check whether it ends with 'ing' or not: ")
print(s1.endswith('ing'))  # True if s1 ends with 'ing', else False

s2 = input("Input a string to check whether it starts with 'a' or not: ")
print(s2.startswith('a'))  # True if s2 starts with 'a', else False

s3 = input("Input a string to capitalize its first letter: ")
print(s3.capitalize())  # Capitalizes only the first character of the string

s4 = input("Input a string to convert to uppercase: ")
print(s4.upper())  # Converts all characters to uppercase

s5 = input("Input a string to convert to lowercase: ")
print(s5.lower())  # Converts all characters to lowercase

s6 = input("Input a string to check if it's all digits: ")
print(s6.isdigit())  # Returns True if all characters are digits

s7 = input("Input a string to check if it's alphabetic only: ")
print(s7.isalpha())  # Returns True if all characters are alphabetic

s8 = input("Input a string to check if it's alphanumeric: ")
print(s8.isalnum())  # Returns True if all characters are alphanumeric

s9 = input("Input a string to check if it's in title case: ")
print(s9.istitle())  # True if string is titlecased (Each Word Starts With Capital)

s10 = input("Input a string to convert it to title case: ")
print(s10.title())  # Converts first letter of each word to uppercase

s11 = input("Input a string to check if it's all uppercase: ")
print(s11.isupper())  # True if all characters are uppercase

s12 = input("Input a string to check if it's all lowercase: ")
print(s12.islower())  # True if all characters are lowercase

s13 = input("Input a string to remove leading and trailing spaces: ")
print(s13.strip())  # Removes spaces from both ends

s14 = input("Input a string to left-strip (remove leading spaces): ")
print(s14.lstrip())  # Removes leading (left-side) spaces

s15 = input("Input a string to right-strip (remove trailing spaces): ")
print(s15.rstrip())  # Removes trailing (right-side) spaces

s16 = input("Input a string to replace 'a' with 'A': ")
print(s16.replace('a', 'A'))  # Replaces all occurrences of 'a' with 'A'

s17 = input("Input a string to count how many times 'a' appears: ")
print(s17.count('a'))  # Counts how many times 'a' appears

s18 = input("Input a string to find index of first 'e': ")
print(s18.find('e'))  # Returns lowest index of 'e'; returns -1 if not found

s19 = input("Input a string to center it in width 20: ")
print(s19.center(20))  # Centers the string within 20 characters wide field

s20 = input("Input a string to swap its case: ")
print(s20.swapcase())  # Swaps uppercase to lowercase and vice versa

s21 = input("Input a string to check if it's whitespace only: ")
print(s21.isspace())  # Returns True if string contains only whitespace

s22 = input("Input a string to check if it is printable: ")
print(s22.isprintable())  # Returns True if all characters are printable

s23 = input("Input a string to check if it's an identifier: ")
print(s23.isidentifier())  # Returns True if it’s a valid identifier (variable name)

s24 = input("Input a string to join with hyphen (-): ").split()
print("-".join(s24))  # Joins a list of strings with '-'

s25 = input("Input a string to partition around first space: ")
print(s25.partition(" "))  # Splits string into 3 parts: before, separator, after

s26 = input("Input a string to split into words: ")
print(s26.split())  # Splits string by spaces into a list of words

s27 = input("Input a string to encode into bytes: ")
print(s27.encode())  # Encodes string into bytes using UTF-8
