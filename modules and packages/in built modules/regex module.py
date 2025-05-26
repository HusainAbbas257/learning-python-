import re

# ----------------------------------------
# re module: Regular Expressions in Python
# ----------------------------------------
# It allows pattern matching, searching, splitting, replacing, etc. in strings.

print("\n>>> Summary of re module:")
print(re.__doc__)  # General description of the re module

# ------------------------------
# 1. re.match()
# ------------------------------
# Match only at the beginning of the string
pattern = r"Hello"
text = "Hello world!"
print("\n>>> re.match")
print(re.match.__doc__)
match_obj = re.match(pattern, text)
print("Match result:", match_obj.group() if match_obj else "No match")

# ------------------------------
# 2. re.search()
# ------------------------------
# Search the entire string for the first match
print("\n>>> re.search")
print(re.search.__doc__)
search_obj = re.search("world", text)
print("Search result:", search_obj.group() if search_obj else "Not found")

# ------------------------------
# 3. re.findall()
# ------------------------------
# Return all non-overlapping matches as a list
print("\n>>> re.findall")
print(re.findall.__doc__)
text2 = "cat, mat, bat, fat"
matches = re.findall(r"\b\w{3}\b", text2)
print("Findall result:", matches)

# ------------------------------
# 4. re.finditer()
# ------------------------------
# Return iterator with match objects
print("\n>>> re.finditer")
print(re.finditer.__doc__)
for match in re.finditer(r"\b\w{3}\b", text2):
    print("Finditer match:", match.group())

# ------------------------------
# 5. re.sub()
# ------------------------------
# Replace pattern with replacement
print("\n>>> re.sub")
print(re.sub.__doc__)
replaced = re.sub("cat", "dog", text2)
print("Substitution result:", replaced)

# ------------------------------
# 6. re.subn()
# ------------------------------
# Like sub, but returns tuple (new_string, number_of_subs)
print("\n>>> re.subn")
print(re.subn.__doc__)
replaced_subn = re.subn("\w{3}", "xxx", text2)
print("Subn result:", replaced_subn)

# ------------------------------
# 7. re.split()
# ------------------------------
# Split string by the occurrences of the pattern
print("\n>>> re.split")
print(re.split.__doc__)
split_result = re.split(", ", text2)
print("Split result:", split_result)

# ------------------------------
# 8. re.compile()
# ------------------------------
# Precompile a regex pattern for reuse
print("\n>>> re.compile")
print(re.compile.__doc__)
compiled_pattern = re.compile(r"\b\w{3}\b")
compiled_matches = compiled_pattern.findall(text2)
print("Compiled pattern matches:", compiled_matches)

# ------------------------------
# 9. re.fullmatch()
# ------------------------------
# Match the entire string (not just a part of it)
print("\n>>> re.fullmatch")
print(re.fullmatch.__doc__)
full_match_result = re.fullmatch(r"Hello world!", text)
print("Fullmatch result:", full_match_result.group() if full_match_result else "No full match")

# ------------------------------
# 10. re.escape()
# ------------------------------
# Escape all special characters in a string
print("\n>>> re.escape")
print(re.escape.__doc__)
special_string = "2 + 2 = 4?"
escaped = re.escape(special_string)
print("Escaped string:", escaped)

# ------------------------------
# 11. re.purge()
# ------------------------------
# Clear internal cache of compiled patterns (rarely used)
print("\n>>> re.purge")
print(re.purge.__doc__)
re.purge()  # No output, just clears the cache
print("Cache cleared with re.purge()")
