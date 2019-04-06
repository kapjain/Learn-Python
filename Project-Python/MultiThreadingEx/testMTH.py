import threading


import time
import datetime
# global variable x 
x = 0
y = 0

def increment1(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1

def increment2(): 
    """ 
    function to increment global variable x 
    """
    global y 
    y += 1
    
def thread_task1(lock): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000):
        lock.acquire() 
        increment1() 
        lock.release()

def thread_task2(lock): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000):
        lock.acquire() 
        increment2() 
        lock.release()
        
def main_task(): 
    global x , y
    # setting global variable x as 0 
    x = 0
    y = 0

    # creating a lock 
    lock = threading.Lock() 

    # creating threads 
    t1 = threading.Thread(target=thread_task1, args=(lock,)) 
    t2 = threading.Thread(target=thread_task2, args=(lock,)) 

    # start threads 
    t1.start() 
    t2.start() 

    # wait until threads finish their job 
    t1.join() 
    t2.join() 

if __name__ == "__main__": 
    print ("%s: %s" % ('start time', datetime.datetime.now()))
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x)) 
        print("Iteration {0}: x = {1}".format(i,y)) 
    print ("%s: %s" % ('end time', datetime.datetime.now())) 
