# in asyncio we were just runnig different task parrallely on same core of cpu 
# but in multi threading we will create multiple threads that use differnent cores 

# example:
import threading
import time

def show(name):
    print(f"Thread {name} started")
    time.sleep(2)
    print(f"Thread {name} finished")

# Create 2 threads
t1 = threading.Thread(target=show, args=("One",))
t2 = threading.Thread(target=show, args=("Two",))

# Start them
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("All threads done!")


# these python threads are shit they just access the same variable for example
x = 0

def increment():
    global x
    for _ in range(1000000):
        x += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final value of x:", x)
# so u dont get 2000000 always but sometimes get som cursed number

# to prevent this we can make each thread use its own copy of the variable as;

x=0
lock = threading.Lock()

def incrementing():
    global x
    for _ in range(1000000):
        with lock:
            x += 1


t1 = threading.Thread(target=incrementing)
t2 = threading.Thread(target=incrementing)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final value of x:", x)


# when u want tpo distributee some work then u think u can use multiple threads? no u are nooob
# u can use pooling it is easy af
from concurrent.futures import ThreadPoolExecutor


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} done")
    return f"{name} result"

with ThreadPoolExecutor(max_workers=3) as executor:
    names = ["Task A", "Task B", "Task C", "Task D"]
    results = executor.map(task, names)

print("Results:", list(results))

# here u are sqaying here is my tasks and u can use max 3 workers now u do ir the way u want
# 4 tasks submitted — first 3 run immediately, 4th waits
