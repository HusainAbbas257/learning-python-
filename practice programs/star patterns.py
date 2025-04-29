# 1.
# *
# **
# ***
# ****
# *****
for i in range(6):
    print("*"*i)
print()

# 2.
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    print("*"*i)
print()

# 3.
# *****
#  ****
#   ***
#    **
#     *
for i in range(6):
    print(" "*i+"*"*(5-i))
print()
# 4.
#     *
#    **
#   ***
#  ****
# *****
for i in range(6):
    print(" "*(5-i)+"*"*i)
print()

# 5.
#     *
#    ***
#   *****
#  *******
# *********
for i in range(6):
    print(" "*(5-i)+"*"*i+"*"*(i-1))
print()

# 6.
# *********
#  *******
#   *****
#    ***
#     *
for i in range(6):
    print(" "*i+"*"*(5-i)+"*"*(4-i))
print()

# 7.
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
for i in range(6):
    print(" "*(5-i)+"*"*i+"*"*(i-1))
for i in range(6):
    print(" "*i+"*"*(5-i)+"*"*(4-i))
print()

# 8.hollow cobe of length n
# *****
# *   *
# *   *
# *   *
# *****
n=5
print("*"*n)
for i in range(n-2):
    print("*"+" "*(n-2)+"*")
print("*"*n)