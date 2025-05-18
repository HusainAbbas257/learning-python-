# all of followings are examples of dictionaries
d1 = {"name": "Alice", "age": 16}
d2 = dict(one=1, two=2)
d3 = {"a": 1, "b": [1, 2], "c": {"x": 10}}
d4 = {}
print(type(d1))
print(type(d2))
print(type(d3))
print(type(d4))

# dictionaries are mutable and store data in key-value pairs
# keys are unique and immutable (strings, numbers, etc)
# values can be anything

# two or more dictionaries can be merged be | operater
dict1={"one":1,"two":2}
dict2={"three":3,'four':4}
newdict=dict1|dict2#merges both dictionaries
print(newdict)#{'one': 1, 'two': 2, 'three': 3, 'four': 4}
#--------------dictionary-methods---------------#

# 1. get(key) -> returns value if key exists, else returns None
info = {"name": "Bob", "country": "Canada"}
print("get name -->", info.get("name"))
print("get age (not present) -->", info.get("age"))  # returns None

# 2. keys() -> returns all keys
print("keys -->", info.keys())

# 3. values() -> returns all values
print("values -->", info.values())

# 4. items() -> returns all key-value pairs as tuples
print("items -->", info.items())

# 5. update(dict) -> updates current dict with another one
info.update({"age": 20, "language": "English"})
print("after update -->", info)

# 6. pop(key) -> removes and returns the value of given key
val = info.pop("country")
print("after pop 'country' -->", info)
print("popped value -->", val)

# 7. popitem() -> removes and returns the last inserted key-value pair
last = info.popitem()
print("after popitem -->", info)
print("last popped item -->", last)

# 8. setdefault(key, value) -> adds key with value if not exists, else returns existing value
d5 = {"x": 100}
res = d5.setdefault("x", 500)  # already exists
print("setdefault existing key -->", res)
res2 = d5.setdefault("y", 200)  # new key
print("setdefault new key -->", res2)
print("d5 now -->", d5)

# 9. del -> deletes a key from dict
sample = {"a": 1, "b": 2, "c": 3}
del sample["b"]
print("after deleting 'b' -->", sample)

# 10. clear() -> removes everything
sample.clear()
print("after clear -->", sample)

#--------------------sample-output-------------------------#
# <class 'dict'>
# <class 'dict'>
# <class 'dict'>
# <class 'dict'>
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# get name --> Bob
# get age (not present) --> None
# keys --> dict_keys(['name', 'country'])
# values --> dict_values(['Bob', 'Canada'])
# items --> dict_items([('name', 'Bob'), ('country', 'Canada')])
# after update --> {'name': 'Bob', 'country': 'Canada', 'age': 20, 'language': 'English'}
# after pop 'country' --> {'name': 'Bob', 'age': 20, 'language': 'English'}
# popped value --> Canada
# after popitem --> {'name': 'Bob', 'age': 20}
# last popped item --> ('language', 'English')
# setdefault existing key --> 100
# setdefault new key --> 200
# d5 now --> {'x': 100, 'y': 200}
# after deleting 'b' --> {'a': 1, 'c': 3}
# after clear --> {}
