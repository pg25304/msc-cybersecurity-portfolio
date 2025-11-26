#Expected result: 2000 items.
#Actual result: Often less than 2000.
# Why? Both threads sometimes try to append at the same time, causing lost writes.
# This is a race condition because the list doesn’t protect itself.
#- Problem: list.append() is not protected by locks. If both threads try to append simultaneously, some writes can be lost.
# Result: You expect 2000 items, but often get fewer because of race conditions.



import threading

numbers = []  # Shared list, A plain Python list shared by both threads.
#Each thread tries to append 1000 items.
def add_numbers():
    for i in range(1000):
        numbers.append(i)  # Not thread-safe
#Two threads run the same function at the same time.
t1 = threading.Thread(target=add_numbers)
t2 = threading.Thread(target=add_numbers)

t1.start()
t2.start()
#- What join() does here: It ensures the main program waits until both threads finish appending to the list.
#- Important: join() only guarantees that the threads finish — it does not fix race conditions.

t1.join()
t2.join()

print("Length of list:", len(numbers))