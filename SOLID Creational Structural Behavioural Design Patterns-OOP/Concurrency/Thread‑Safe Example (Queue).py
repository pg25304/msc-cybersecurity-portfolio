import queue
import threading

# Thread-safe queue - - queue.Queue comes from Python’s standard library module called queue.
q = queue.Queue()

numbers = []
def add_number():
    for i in range(1000):
        #- Adds items to the queue. Internally, the queue uses locks so only one thread can modify it at a time.
        q.put(i)

#Both threads safely add items without interfering.
#- threading is one of these modules, and inside it you’ll find threading.Thread

t1 = threading.Thread(target=add_number())
t2 = threading.Thread(target=add_number())

t1.start()
t2.start()
#- In Python, join() is a synchronisation method used with threads (threading.Thread)
# and processes (multiprocessing.Process).
#It makes the main program wait until the thread or process you called join() on has finished running

#- What join() does here: It ensures the main program waits until both threads finish appending to the list.

t1.join()
t2.join()
#- Retrieves all items from the queue and puts them into the numbers list.
print(f"Length of queue: {q.qsize()}")

#q.qsize()
# Belongs to: queue.Queue objects (from the queue module).
# Purpose: Returns the approximate number of items currently in the queue.

