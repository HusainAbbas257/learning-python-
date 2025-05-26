import time

# ------------------------------
# Summary of time module
# ------------------------------
print("\n>>> Summary of time module:")
print(time.__doc__)  # General description of the time module

# ------------------------------
# 1. time()
# ------------------------------
# Returns the current time in seconds since the Epoch (Unix time)
print("\n>>> Function: time.time")
print(time.time.__doc__)
current_time = time.time()
print(f"Current time (in seconds since Epoch): {current_time}")

# ------------------------------
# 2. sleep()
# ------------------------------
# Suspends (pauses) execution for the given number of seconds
print("\n>>> Function: time.sleep")
print(time.sleep.__doc__)
print("Sleeping for 2 seconds...")
start_sleep = time.time()
time.sleep(2)
end_sleep = time.time()
print(f"Slept for {end_sleep - start_sleep:} seconds")

# ------------------------------
# 3. ctime()
# ------------------------------
# Converts a time expressed in seconds since the epoch to a string
print("\n>>> Function: time.ctime")
print(time.ctime.__doc__)
print("Human-readable time:", time.ctime(current_time))

# ------------------------------
# 4. gmtime() and localtime()
# ------------------------------
# gmtime() - Converts epoch to UTC struct_time
# localtime() - Converts epoch to local timezone struct_time
print("\n>>> Function: time.gmtime & time.localtime")
print(time.gmtime.__doc__)
print(time.localtime.__doc__)
utc_struct = time.gmtime(current_time)
local_struct = time.localtime(current_time)
print("UTC time struct:", utc_struct)
print("Local time struct:", local_struct)

# ------------------------------
# 5. mktime()
# ------------------------------
# Converts a struct_time back to seconds since epoch
print("\n>>> Function: time.mktime")
print(time.mktime.__doc__)
epoch_from_local = time.mktime(local_struct)
print("Epoch from local struct_time:", epoch_from_local)

# ------------------------------
# 6. asctime()
# ------------------------------
# Converts a struct_time to a readable string
print("\n>>> Function: time.asctime")
print(time.asctime.__doc__)
print("Readable time from struct_time:", time.asctime(local_struct))

# ------------------------------
# 7. strftime() - format struct_time to string
# ------------------------------
print("\n>>> Function: time.strftime")
print(time.strftime.__doc__)
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_struct)
print("Formatted time:", formatted)

# ------------------------------
# 8. strptime() - parse string to struct_time
# ------------------------------
print("\n>>> Function: time.strptime")
print(time.strptime.__doc__)
parsed_time = time.strptime("2025-05-26 12:00:00", "%Y-%m-%d %H:%M:%S")
print("Parsed struct_time:", parsed_time)

# ------------------------------
# 9. monotonic()
# ------------------------------
# Monotonic clock can't go backwards (used for benchmarking)
print("\n>>> Function: time.monotonic")
print(time.monotonic.__doc__)
mono_start = time.monotonic()
time.sleep(1)
mono_end = time.monotonic()
print(f"Monotonic time passed: {mono_end - mono_start:} seconds")

# ------------------------------
# 10. perf_counter()
# ------------------------------
# High precision timer (for benchmarking, better than time.time())
print("\n>>> Function: time.perf_counter")
print(time.perf_counter.__doc__)
perf_start = time.perf_counter()
time.sleep(1)
perf_end = time.perf_counter()
print(f"Performance counter time passed: {perf_end - perf_start:.6f} seconds")

# ------------------------------
# 11. process_time()
# ------------------------------
# Measures CPU time (doesn't count sleep)
print("\n>>> Function: time.process_time")
print(time.process_time.__doc__)
proc_start = time.process_time()
for _ in range(1000000): pass  # Some CPU work
duration = time.process_time() - proc_start
print(f"Process (CPU) time used: {duration:} seconds")
