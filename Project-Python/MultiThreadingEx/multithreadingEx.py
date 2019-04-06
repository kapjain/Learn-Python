"""
Threading is one of the most well known approaches to attaining Python concurrency and parallelism. Threading is a feature usually provided by the operating system. Threads are lighter than processes, and share the same memory space.

Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.


Starting a New Thread
To spawn another thread, you need to call the following method available in the thread module 
_thread.start_new_thread ( function, args[, kwargs] )

args is a tuple of arguments; use an empty tuple to call function without passing any arguments. kwargs is an optional dictionary of keyword arguments.
"""


import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print ("Error: unable to start thread")

while 1:
    pass

"""
Thread-1: Thu Dec 21 23:32:14 2017
Thread-2: Thu Dec 21 23:32:16 2017
Thread-1: Thu Dec 21 23:32:16 2017
Thread-1: Thu Dec 21 23:32:18 2017
Thread-2: Thu Dec 21 23:32:20 2017
Thread-1: Thu Dec 21 23:32:20 2017
Thread-1: Thu Dec 21 23:32:22 2017
Thread-2: Thu Dec 21 23:32:24 2017
Thread-2: Thu Dec 21 23:32:28 2017
Thread-2: Thu Dec 21 23:32:32 2017
"""


import threading


exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time1(self.name, self.counter, 5)
        print ("Exiting " + self.name)

def print_time1(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


"""
Starting Thread-1
Starting Thread-2
Thread-1: Thu Dec 21 23:56:54 2017
Thread-2: Thu Dec 21 23:56:55 2017
Thread-1: Thu Dec 21 23:56:55 2017
Thread-1: Thu Dec 21 23:56:56 2017
Thread-2: Thu Dec 21 23:56:57 2017
Thread-1: Thu Dec 21 23:56:57 2017
Thread-1: Thu Dec 21 23:56:58 2017
Exiting Thread-1
Thread-2: Thu Dec 21 23:56:59 2017
Thread-2: Thu Dec 21 23:57:01 2017
Thread-2: Thu Dec 21 23:57:03 2017
Exiting Thread-2
Exiting Main Thread
"""