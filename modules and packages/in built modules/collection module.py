from collections import Counter, defaultdict, deque, namedtuple, ChainMap

print("=== PYTHON COLLECTIONS MODULE ===\n")

#-------------------------------------1. COUNTER - Count stuff easily-----------------------------------------
# 
print("1. COUNTER - For counting things")
print("-" * 40)

# Count letters in text
text = "programming"
letter_count = Counter(text)
print(f"Letters in '{text}': {letter_count}")

# Count items in a list
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_count = Counter(fruits)
print(f"Fruit count: {fruit_count}")

# Get most common items
print(f"Most common: {fruit_count.most_common(2)}")

#----------------------------------------2. DEFAULTDICT - Never get KeyError again-------------------------------------------
print("2. DEFAULTDICT - Automatic default values")
print("-" * 40)

# Group students by grade
students = [
    ('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), 
    ('Diana', 'B'), ('Eve', 'A')
]

# Normal dict way (messy)
normal_groups = {}
for name, grade in students:
    if grade not in normal_groups:
        normal_groups[grade] = []
    normal_groups[grade].append(name)

# defaultdict way (clean)
grade_groups = defaultdict(list)
for name, grade in students:
    grade_groups[grade].append(name)

print(f"Groups: {dict(grade_groups)}")

# Count with defaultdict
text_count = defaultdict(int)
for char in "python is getting boring af":
    text_count[char] += 1
print(f"Character count: {dict(text_count)}")
print()


#-------------------------------------------3. DEQUE - Fast operations on both ends-------------------------------------------- 

print("3. DEQUE - Super fast list for both ends")
print("-" * 40)

# Create a deque
queue = deque([1, 2, 3])
print(f"Initial: {queue}")

# Add to both ends
queue.appendleft(0)    # Add to left
queue.append(4)        # Add to right
print(f"After adding: {queue}")

# Remove from both ends
left_item = queue.popleft()   # Remove from left
right_item = queue.pop()      # Remove from right
print(f"Removed {left_item} and {right_item}, remaining: {queue}")

# Rotate (shift elements)
queue.rotate(1)  # Move right
print(f"After rotate: {queue}")

# cool example: Sliding window of recent items
recent_actions = deque(maxlen=3)  # Only keep last 3
actions = ['login', 'view_page', 'click_button', 'submit_form', 'logout']
for action in actions:
    recent_actions.append(action)
    print(f"Recent actions: {list(recent_actions)}")
print()


# -----------------------------------4. NAMEDTUPLE - Easy way to create simple classes-----------------------------------

print("4. NAMEDTUPLE - Simple objects with names")
print("-" * 40)

# Create a Person class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
alice = Person('Alice', 25, 'New York')
bob = Person('Bob', 30, 'London')

print(f"Alice: {alice}")
print(f"Alice's name: {alice.name}")
print(f"Alice's age: {alice[1]}")  # Can use index too

# Create from list
data = ['Charlie', 35, 'Paris']
charlie = Person._make(data)
print(f"Charlie: {charlie}")

# Change some values (creates new object)
older_alice = alice._replace(age=26)
print(f"Older Alice: {older_alice}")

#-------------------------------------5. CHAINMAP - Combine multiple dictionaries-------------------------------------

print("5. CHAINMAP - Combine multiple dicts")
print("-" * 40)

# Different configuration levels
defaults = {'color': 'blue', 'size': 'medium', 'debug': False}
user_settings = {'color': 'red', 'size': 'large'}
temp_override = {'debug': True}

# Combine them (first dict wins for conflicts)
config = ChainMap(temp_override, user_settings, defaults)
print(f"Final config: {dict(config)}")
print(f"Color: {config['color']}")  # From user_settings
print(f"Debug: {config['debug']}")  # From temp_override
print(f"Size: {config['size']}")    # From user_settings

# Add new settings (only affects first dict)
config['new_feature'] = True
print(f"Temp override after change: {temp_override}")
print()

