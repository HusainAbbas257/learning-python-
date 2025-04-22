# all of the followings are examples of sets
s1 = {1, 2, 3, 4, 5}
s2 = {"python", "is", "best"}
s3 = {1, "two", 3.0, True}
s4 = set()  # empty set (not {} – that's an empty dictionary)
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

# sets are unordered and do not allow duplicate values
s5 = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed -->", s5)

#-------------set-methods--------------#

# 1. add() -> adds one element to the set
s6 = {1, 2, 3}
s6.add(4)
print("after adding 4 -->", s6)

# 2. update() -> adds multiple elements (from another set, list, etc.)
s6.update([5, 6, 7])
print("after updating with [5,6,7] -->", s6)

# 3. remove(value) -> removes a value (raises error if not found)
s6.remove(3)
print("after removing 3 -->", s6)

# 4. discard(value) -> removes a value (does not raise error if not found)
s6.discard(10)
print("after discarding 10 (no error) -->", s6)

# 5. pop() -> removes and returns a random element
val = s6.pop()
print("after popping random value:", val, "-->", s6)

# 6. clear() -> removes all elements
s7 = {10, 20, 30}
s7.clear()
print("after clearing set -->", s7)

# 7. union() -> returns a new set with all items from both sets
a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print("union of a and b -->", c)

# 8. intersection() -> common elements in both sets
i = a.intersection(b)
print("intersection of a and b -->", i)

# 9. difference() -> elements in one set but not the other
d = a.difference(b)
print("difference of a - b -->", d)

# 10. issubset(), issuperset(), isdisjoint()
print("Is a subset of c? -->", a.issubset(c))
print("Is c a superset of b? -->", c.issuperset(b))
print("Are a and b disjoint? -->", a.isdisjoint(b))

#---------------sample-output---------------#
# <class 'set'>
# <class 'set'>
# <class 'set'>
# <class 'set'>
# Set with duplicates removed --> {1, 2, 3, 4, 5}
# after adding 4 --> {1, 2, 3, 4}
# after updating with [5,6,7] --> {1, 2, 3, 4, 5, 6, 7}
# after removing 3 --> {1, 2, 4, 5, 6, 7}
# after discarding 10 (no error) --> {1, 2, 4, 5, 6, 7}
# after popping random value: 1 --> {2, 4, 5, 6, 7}
# after clearing set --> set()
# union of a and b --> {1, 2, 3, 4, 5}
# intersection of a and b --> {3}
# difference of a - b --> {1, 2}
# Is a subset of c? --> True
# Is c a superset of b? --> True
# Are a and b disjoint? --> False
