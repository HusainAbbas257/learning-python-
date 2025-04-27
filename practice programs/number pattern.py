# 1.
# 0 0 0 0 0 0 
# 1 1 1 1 1 1 
# 2 2 2 2 2 2 
# 3 3 3 3 3 3 
# 4 4 4 4 4 4 
# 5 5 5 5 5 5 
for i in range(6):
    for j in range(6):
        print(i,end=' ')
    print()
print()

# 2.
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 

for i in range(6):
    for j in range(6):
        print(j,end=' ')
    print()
print()

# 3.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print()
print()

# 3.
# 0 
# 0 1 
# 0 1 2 
# 0 1 2 3 
# 0 1 2 3 4 
for i in range(6):
    for j in range(i):
        print(j,end=' ')
    print()
print()

# 4.
#  00000
#  11111
#   2222
#    333
#     44
#      5
for i in range(6):
    for j in range(i):
        print(end=' ')
    for j in range(6,i,-1):
        print(i,end='')
    print()
print()
# 5.
# 654321
#  65432
#   6543
#    654
#     65
#      6

for i in range(6):
    for j in range(i):
        print(end=' ')
    for j in range(6,i,-1):
        print(j,end='')
    print()
print()
# 6.
# 012345
#  01234
#   0123
#    012
#     01
#      0
for i in range(6):
    print(" "*i,end='')
    for j in range(6-i):
        print(j,end='')
    print()
print()

# 7.
#     1
#    22
#   333
#  4444
# 55555
for i in range(6):
    
    print(' '*(5-i),end='')
    for j in range(i):
        print(i,end='')
    print()
print()

# 8.
#     0
#    01
#   012
#  0123
# 01234
for i in range(6):
    
    print(' '*(5-i),end='')
    for j in range(i):
        print(j,end='')
    print()
print()

# 9.
#     1
#    121
#   12321
#  1234321
# 123454321
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
print()

# 10.
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21 
num =1
for i in range(6):
    for i in range(i+1):
        print(f'{num} ',end='')
        num+=1
    print()
print()