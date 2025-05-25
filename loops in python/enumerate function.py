# as we know we can iterate throgh a list as:
lst=[3,8,1,0,2,5,6,9,4,7]
for i in lst:
    print(i)
print("\n")
# but what if we have to access the indexing at the perticular point for example we need to find index of largest number in the list:
lst=[3,8,1,0,2,5,6,9,4,7]
large=0
large_index=-1
for i in range(len(lst)):
    if lst[i]>large:
        large_index=i
        large=lst[i]
print(large_index,large)
print("\n")

# this also can be achieved more properly using enumerate() function as:
large=0
large_index=-1
for index,value in enumerate(lst):#here index is the index and value is the value in lst at that index
    if(value>large):
        large_index=index
        large=value
print(large_index,large)
print("\n")