#The purpose of this code is to demonstrate the difference between synchronous (blocking)
# execution and asynchronous (non-blocking) execution using threads in Python.

import time
import threading
#time: used for delays (sleep).
#threading: used for running tasks asynchronously (in separate threads).
def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)
#Defines a function wait_and_print: Waits for 1 second (time.sleep(1.0)).
#Prints the message msg.
def wait_and_print_async(msg):
    def callback():
        print(msg)

    # callback is a function you defined inside wait_and_print_async.
    # It’s called a nested function (or inner function).
    # You pass this callback function to threading.Timer so that it runs after 1 second.
    timer = threading.Timer(1.0, callback)#This creates a thread that waits 1 second
    # and then runs callback() without blocking the main program.
    # So while the timer is waiting, your main program can continue doing other things.
    timer.start() #Starts the timer

if __name__ == "__main__":
    wait_and_print("First call (blocking)")
    wait_and_print("Second call (blocking)")
    #These are blocking calls (run sequentially)

    wait_and_print_async("First call (non-blocking)")
    wait_and_print_async("Second call (non-blocking)")
    #These schedule printing after 1 second without blocking the main thread.



"""wait_and_print(msg)
Simulates a delay (1 second) and then prints a message.
Runs synchronously: the program waits for each call to finish before moving to the next.
wait_and_print_async(msg)
Uses threading.Timer to schedule a function (callback) that prints the message after 1 second.
Runs asynchronously: the main program does not wait; it continues immediately while the timer
 runs in a separate thread."""
