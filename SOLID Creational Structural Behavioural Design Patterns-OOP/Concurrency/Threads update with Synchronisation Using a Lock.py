#What happens:
# Now the result is always 200000.
# The lock ensures only one thread updates counter at a time.
# This prevents race conditions and guarantees correctness.

import threading

counter = 0
lock = threading.Lock()  # Synchronisation tool

def increment():
    global counter
    for _ in range(100000):
        with lock:        # Only one thread can enter here at a time
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final counter:", counter)