#- Imports Python’s threading module, which allows us to create and manage threads.
import threading
#- Defines a class SafeCounter.
# self.value = 0 → the counter starts at zero.
# self.lock = threading.Lock() → creates a lock to protect access to value.
class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
#- increment() increases the counter by 1.
#with self.lock: → ensures only one thread at a time can execute the increment.
#This prevents race conditions (two threads trying to update value simultaneously).

    def increment(self):
        with self.lock:
            self.value += 1

#client code
counter = SafeCounter() # - Creates an instance of SafeCounter.
#- Creates 100 threads, each assigned to run counter.increment.
threads = [threading.Thread(target=counter.increment) for _ in range(100)]
##- Starts all threads.
#- Waits for all threads to finish before moving on.
#Ensures the program doesn’t print the result until all increments are complete.
for t in threads: t.start()
for t in threads: t.join()
print("counter:", counter.value) #- Prints the final value of the counter.
#- Because of the lock, the final value is guaranteed to be 100.
#Without the lock, the final value could be less than 100 due to race conditions.