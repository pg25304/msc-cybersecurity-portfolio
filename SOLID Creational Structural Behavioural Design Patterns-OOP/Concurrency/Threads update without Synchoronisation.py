#What happens:
# You expect counter to be 200000 (100000 + 100000).
# But often you’ll get a smaller number — because both threads sometimes try to update counter at the same time.
# This is a race condition: the result depends on unpredictable timing.

import threading

# Shared resource
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

# Two threads increment the counter
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final counter:", counter)