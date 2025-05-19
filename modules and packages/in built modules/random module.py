import random


# Getting a random float between 0 and 1
rand_float = random.random()
print("Random float between 0 and 1:", rand_float)

# Getting a random float in a range
start = float(input("Enter start of range for random float: "))
end = float(input("Enter end of range for random float: "))
rand_uniform = random.uniform(start, end)
print(f"Random float between {start} and {end}:", rand_uniform)

# Getting a random integer in a range
low = int(input("Enter lower bound for random integer: "))
high = int(input("Enter upper bound for random integer: "))
rand_int = random.randint(low, high)
print(f"Random integer between {low} and {high}:", rand_int)

# Random choice from a list
items = input("Enter list items separated by commas: ").split(',')
for i in range(len(items)):
    items[i] = items[i].strip()
rand_choice = random.choice(items)
print("Random choice from your list:", rand_choice)

# Shuffle a list
print("Original list:", items)
random.shuffle(items)
print("Shuffled list:", items)

# Random sample of multiple items
sample_size = int(input("Enter number of items to randomly sample from your list: "))
if sample_size <= len(items):
    sample = random.sample(items, sample_size)
    print("Random sample:", sample)
else:
    print("Sample size is larger than the list length! Cannot perform sampling.")


#----------------------sample-output----------------------#
# Random float between 0 and 1: 0.09723960231647233
# Enter end of range for random float: 99.99
# Random float between 33.33 and 99.99: 35.981279093811594
# Enter lower bound for random integer: 33
# Enter upper bound for random integer: 100
# Random integer between 33 and 100: 93
# Enter list of items : 10,9,8,7,6,5,4,3,2,1,0
# Random choice from your list: ,
# Original list: ['1', '0', ',', '9', ',', '8', ',', '7', ',', '6', ',', '5', ',', '4', ',', '3', ',', '2', ',', '1', ',', '0']
# Shuffled list: [',', '7', '1', '0', ',', ',', ',', '3', ',', '5', '4', '6', ',', '8', '9', ',', '0', ',', '2', '1', ',', ',']
# Enter number of items to randomly sample from your list: 10
# Random sample: [',', '2', '1', ',', '0', '0', ',', '3', '6', '1']
# PS C:\Users\DELL\Desktop\learning-python-\modules and packages\in built modules> python '.\random module.py'
# Random float between 0 and 1: 0.9461800972533252
# Enter start of range for random float: 33.33
# Enter end of range for random float: 99.99
# Random float between 33.33 and 99.99: 92.10280226304678
# Enter lower bound for random integer: 33
# Enter upper bound for random integer: 100
# Random integer between 33 and 100: 38
# Enter list items separated by commas: 10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10
# Random choice from your list: -6
# Original list: ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-10']
# Shuffled list: ['-5', '2', '-2', '5', '6', '-3', '-6', '3', '-4', '-7', '-1', '9', '-9', '4', '-10', '10', '0', '1', '7', '-8', '8']
# Enter number of items to randomly sample from your list: 5 
# Random sample: ['-9', '-7', '9', '8', '-3']