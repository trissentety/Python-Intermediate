from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available. gets two arguments queue and lock. get first value in queue

        # do stuff...proccessing
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()
        #no daemon
        #if ....:
            #break


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock)) #target func, tuple comma
        thread.daemon = True  # dies when the main thread dies. default isn't daemon thread
        thread.start()
    
    # fill the queue with items
    for x in range(1, 21):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done') #when this statement is reached all threads die cause of daemon, while True no longer gets evoked

#what's important is queue can easily exchange data in a thread safe environment

# main done