list = ["this is a", "list", 123, 3.14, False]
# a list is a collection of any datatype in a single variable

print(list)
# prints --> ['this is a', 'list', 123, 3.14, False]

# indexing is same as strings (it starts from 0)
# unlike strings, it is mutable. For example:
list[0] = "python"
list[1] = "is"
list[2] = "fun"
list[3] = "its"
list[4] = True
print(list)
# prints ---> ['python', 'is', 'fun', 'its', True]

##-----------list-methods-------------#

# 1. sort() -> sorts the list (in place)
l1 = [45, 365, 2, 72, 6, 14, 754, 26]
print("before sorting -->", l1)
l1.sort()
print("after sorting -->", l1)

# 2. append() -> adds one element at the end
l2 = [1, 2, 3]
l2.append(4)
print("after appending 4 -->", l2)

# 3. extend() -> adds multiple elements
l3 = [10, 20]
l3.extend([30, 40])
print("after extending with [30, 40] -->", l3)

# 4. insert(index, value)
l4 = ["a", "b", "d"]
l4.insert(2, "c")
print("after inserting 'c' -->", l4)

# 5. remove(value)
l5 = [1, 2, 2, 3]
l5.remove(2)
print("after removing 2 -->", l5)

# 6. pop()
l6 = ["x", "y", "z"]
print("popped element:", l6.pop())
print("after pop -->", l6)

# 7. clear()
l7 = [1, 2, 3]
l7.clear()
print("after clear -->", l7)

# 8. index(value)
l8 = ["apple", "banana", "cherry"]
print("index of banana -->", l8.index("banana"))

# 9. count(value)
l9 = [1, 2, 2, 3, 2]
print("count of 2 -->", l9.count(2))

# 10. reverse()
l10 = [1, 2, 3]
l10.reverse()
print("after reverse -->", l10)

# 11. copy()
l11 = [100, 200]
l12 = l11.copy()
l12.append(300)
print("original -->", l11)
print("copy with change -->", l12)

# 12. slicing
lst = [10, 20, 30, 40, 50, 60, 70]
print("slice [2:5] -->", lst[2:5])
print("slice [::2] (skip 1) -->", lst[::2])
print("slice [-3:] (last 3 items) -->", lst[-3:])

#--------------------sample-output-------------------------#
# ['this is a', 'list', 123, 3.14, False]
# ['python', 'is', 'fun', 'its', True]
# before sorting --> [45, 365, 2, 72, 6, 14, 754, 26]
# after sorting --> [2, 6, 14, 26, 45, 72, 365, 754]
# after appending 4 --> [1, 2, 3, 4]
# after extending with [30, 40] --> [10, 20, 30, 40]
# after inserting 'c' --> ['a', 'b', 'c', 'd']
# after removing 2 --> [1, 2, 3]
# popped element: z
# after pop --> ['x', 'y']
# after clear --> []
# index of banana --> 1
# count of 2 --> 3
# after reverse --> [3, 2, 1]
# original --> [100, 200]
# copy with change --> [100, 200, 300]
# slice [2:5] --> [30, 40, 50]
# slice [::2] (skip 1) --> [10, 30, 50, 70]
# slice [-3:] (last 3 items) --> [50, 60, 70]
