# until now we were using thraeds for parrallel calculation but it is a white lie
# there is no efficiency in threads they just get executed one by one because of something called GIl
# to solve this problem here is our true multiprocessing 

from multiprocessing import Process
import time

def heavy_task(name):
    print(f" {name} started")
    time.sleep(2)
    print(f"{name} done")

if __name__ == '__main__':
    p1 = Process(target=heavy_task, args=('Task 1',))
    p2 = Process(target=heavy_task, args=('Task 2',))
    t=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"All done in {time.time()-t}")



# like thread pooling we can pool processses
from multiprocessing import Pool


def square(n):
    time.sleep(1)
    return n * n

if(__name__=='__main__'):
    nums = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:
        results = pool.map(square, nums)
    print(results)

# in multiprocessing elements dont have a shared variable instead have their own to solve it we can use value as:
from multiprocessing import  Value


def increment(shared_num):
    for _ in range(5):
        time.sleep(0.5)
        shared_num.value += 1

if __name__ == '__main__':
    num = Value('i', 0)  # 'i' = integer

    p1 = Process(target=increment, args=(num,))
    p2 = Process(target=increment, args=(num,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Final value: {num.value}")



# or we can use arrays stolen from other languages
from multiprocessing import  Array

def square_all(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]

if __name__ == '__main__':
    numbers = Array('i', [1, 2, 3, 4])

    p = Process(target=square_all, args=(numbers,))
    p.start()
    p.join()

    print(list(numbers))  #  [1, 4, 9, 16]


# or tasks
from multiprocessing import Queue

def worker(q):
    q.put("Work done!")

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  #  reads from queue
    p.join()


# When 2+ processes try to access or change the same variable at the same time...
#Boom! Data corruption. Wrong values. Inconsistent results.
from multiprocessing import  Value


def increment(x):
    for _ in range(1000):
        x.value += 1

if __name__ == '__main__':
    count = Value('i', 0)
    p1 = Process(target=increment, args=(count,))
    p2 = Process(target=increment, args=(count,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Final count:", count.value)  #  NOT 2000! some cursed value 

# to  pre3vent this chaos we use:
from multiprocessing import Lock

def increment(x, lock):
    for _ in range(1000):
        with lock:  #  This line SAVES LIVES
            x.value += 1

if __name__ == '__main__':
    count = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increment, args=(count, lock))
    p2 = Process(target=increment, args=(count, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Final count:", count.value)  #  2000 for real


