# all of followings are examples of tuples
t1=(1,2,3,4,5,6,7,8,9,0)
t2=("python","is","best")
t3=("one",2,True)
t4=()
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

#unlike s it is immutable
# t2(0)=3 #gives error beacuse tuples are immutable ie cannot be changed

#--------------tuple-methods---------------#
#tuples have almost same methods as s but they return a value so the must be called into any otheer tuple

# 1 index(value) -> returns first index of value
t5 = ("apple", "banana", "cherry")
ind = t5.index("banana")
print("index of 'banana' -->", ind)

# 2. count(value) -> returns count of how many times value appears
t6= (1, 2, 2, 3, 2, 4)
cnt = t6.count(2)
print("count of 2 in tuple -->", cnt)



# 3. len() -> not a method but a built-in function to get length
length = len(t6)
print("length of t6 -->", length)

# 4. sorted() -> returns a new sorted tuple (original stays unchanged) and it can be converted into a tuple
t7 = (5, 2, 9, 1)
t8 = tuple(sorted(t7))
print("original tuple -->", t7)
print("sorted copy -->", t8)

# 5. max() / min() -> gives largest / smallest element
nums = (10, 55, 32, 89)
print("maximum number -->", max(nums))
print("minimum number -->", min(nums))

# 6. sum() -> adds up all numeric elements
print("sum of nums -->", sum(nums))

#7.concatebation ->they can be concatenated with + operater
t9=(1,2,3,4,5)
t10=(6,7,8,9,10)
ts=t9+t10
print(ts)

# 8.membership-> you can check if an item exist or not in a tuple by in keyword
print(2 in t9)
print(2 in t10)

# 9.slicing -> slicing of tuple is done in a same way as string

new_ts = ts[3:7]

print("Sliced tuple (without skipping):", new_ts)
new_ts_skipped = ts[2:8:2]
print("Sliced string (with skipping):", new_ts_skipped)

#10.unpacking->tuples can be unpaced into individual variables
a,b,c,d,e,f,g,h,i,j=ts
print(a,b,c,d,e,f,g,h,i,j)

#--------------------sample-output-------------------------#
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>
# index of 'banana' --> 1
# count of 2 in tuple --> 3
# length of t6 --> 6
# original tuple --> (5, 2, 9, 1)
# sorted copy --> (1, 2, 5, 9)
# maximum number --> 89
# minimum number --> 10
# sum of nums --> 186
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# True
# False
# Sliced tuple (without skipping): (4, 5, 6, 7)
# Sliced string (with skipping): (3, 5, 7)
# 1 2 3 4 5 6 7 8 9 10