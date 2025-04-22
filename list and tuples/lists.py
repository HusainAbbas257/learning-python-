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

#-----------list-methods-------------#

# 1. sort() -> sorts the list (in place)
l1 = [45, 365, 2, 72, 6, 14, 754, 26]
print("before sorting -->", l1)
l1.sort()
print("after sorting -->", l1)

# 2. append() -> adds one element at the end
l3 = [1, 2, 3]
print("before appending -->", l3)
l3.append(4)
print("after appending 4 -->", l3)

# 3. extend() -> adds elements from another iterable (like list) to the current list
l4 = [10, 20]
l4.extend([30, 40])
print("after extending with [30, 40] -->", l4)

# 4. insert(index, value) -> inserts element at specific index
l5 = ["a", "b", "d"]
l5.insert(2, "c")
print("after inserting 'c' at index 2 -->", l5)

# 5. remove(value) -> removes first occurrence of value
l6 = [1, 2, 3, 2, 4]
l6.remove(2)
print("after removing first occurrence of 2 -->", l6)

# 6. pop([index]) -> removes and returns element at index (last if not given)
l7 = ["x", "y", "z"]
item = l7.pop()
print("after popping last element -->", l7, "popped:", item)
item2 = l7.pop(0)
print("after popping index 0 -->", l7, "popped:", item2)

# 7. clear() -> removes all elements from list
l8 = [100, 200, 300]
l8.clear()
print("after clearing list -->", l8)

# 8. index(value) -> returns first index of value
l9 = ["apple", "banana", "cherry"]
i = l9.index("banana")
print("index of 'banana' -->", i)

# 9. count(value) -> returns count of how many times value appears
l10 = [1, 2, 2, 3, 2, 4]
cnt = l10.count(2)
print("count of 2 in list -->", cnt)

# 10. reverse() -> reverses the list in place
l11 = [1, 2, 3, 4]
l11.reverse()
print("after reversing -->", l11)

# 11. copy() -> returns a shallow copy of the list
l12 = ["copy", "me"]
l13 = l12.copy()
l13.append("new")
print("original list -->", l12)
print("copied and modified list -->", l13)

# 12. len() -> not a method but a built-in function to get length
length = len(l13)
print("length of l13 -->", length)

# 13. sorted() -> returns a new sorted list (original stays unchanged)
l14 = [5, 2, 9, 1]
l15 = sorted(l14)
print("original list -->", l14)
print("sorted copy -->", l15)

# 14. max() / min() -> gives largest / smallest element
nums = [10, 55, 32, 89]
print("maximum number -->", max(nums))
print("minimum number -->", min(nums))

# 15. sum() -> adds up all numeric elements
print("sum of nums -->", sum(nums))


#------------------sample output-----------#
# ['this is a', 'list', 123, 3.14, False]
# ['python', 'is', 'fun', 'its', True]
# before sorting --> [45, 365, 2, 72, 6, 14, 754, 26]
# after sorting --> [2, 6, 14, 26, 45, 72, 365, 754]
# before appending --> [1, 2, 3]
# after appending 4 --> [1, 2, 3, 4]
# after extending with [30, 40] --> [10, 20, 30, 40]
# after inserting 'c' at index 2 --> ['a', 'b', 'c', 'd']
# after removing first occurrence of 2 --> [1, 3, 2, 4]
# after popping last element --> ['x', 'y'] popped: z
# after popping index 0 --> ['y'] popped: x
# after clearing list --> []
# index of 'banana' --> 1
# count of 2 in list --> 3
# after reversing --> [4, 3, 2, 1]
# original list --> ['copy', 'me']
# copied and modified list --> ['copy', 'me', 'new']
# length of l13 --> 3
# original list --> [5, 2, 9, 1]
# sorted copy --> [1, 2, 5, 9]
# maximum number --> 89
# minimum number --> 10
# sum of nums --> 186