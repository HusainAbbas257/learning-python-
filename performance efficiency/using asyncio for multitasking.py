import asyncio  # this is the async module 

# async function to simulate studying
async def study():
    print('studying started ...')
    await asyncio.sleep(5)  # pause for 5 seconds without blocking the whole program 
    print('studying ended')

# another async function that depends on study()
async def cook():
    print("started cooking")
    await study()  # waiting for studying to finish before continuing 
    print("ended cooking")

# entry point to run the async event loop
asyncio.run(cook())  # runs the top-level async function 

print()
# we can also await multiple tasks as:

# define all tasks as async functions

async def cook():
    print(" Cooking started...")
    await asyncio.sleep(5)
    print("Cooking done!")

async def study():
    print("Studying started...")
    await asyncio.sleep(3)
    print(" Studying done!")

async def wash_dishes():
    print(" Washing dishes started...")
    await asyncio.sleep(2)
    print(" Dishes done!")

async def main():
    # run all the tasks at once like a Game
    await asyncio.gather(
        cook(),
        study(),
        wash_dishes()
    )

asyncio.run(main())


# there is better way to await multipklle tasks :
print()
async def pray():
    print(" Doing namaz...")
    await asyncio.sleep(2)
    print(" Namaz done!")

async def revise_notes():
    print(" Revising notes...")
    await asyncio.sleep(4)
    print(" Notes revised!")

async def main():
    # Create separate independent tasks
    task1 = asyncio.create_task(pray())
    task2 = asyncio.create_task(revise_notes())

    print(" Doing side work while others grind...")

    # You can stilll await them if you want
    await task1
    await task2

asyncio.run(main())


# task can be cancelled as:
print()
async def long_task():
    print(" Task started...")
    try:
        for i in range(10):
            print(f"Working... step {i}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(" Task got cancelled! Cleaning up...")
        # do any cleanup here if needed
        raise  # important to re-raise so cancellation propagates
    print("Task completed!")

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(3)  # Let task run a bit
    print("Time to cancel the task!")
    task.cancel()  # Send cancel signal

    try:
        await task
    except asyncio.CancelledError:
        print("Main caught task cancellation")

asyncio.run(main())



# we can set a time limit for our codes:
print()
async def slow_task():
    print("Starting slow task...")
    await asyncio.sleep(10)  # pretending to be slow af
    print("Slow task finished")

async def main():
    try:
        # Wait max 3 seconds for slow_task to finish
        await asyncio.wait_for(slow_task(), timeout=3)
    except asyncio.TimeoutError:
        print("Task took too long, timeout triggered!")

asyncio.run(main())
