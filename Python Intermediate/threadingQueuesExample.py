from threading import Thread, Lock, current_thread
from queue import Queue

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


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock)) #target func
        t.daemon = True  # dies when the main thread dies. default isn't daemon thread
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

#     in Thread1 got 0
# in Thread1 got 1
# in Thread1 got 2
# in Thread1 got 3
# in Thread1 got 4
# in Thread1 got 5
# in Thread1 got 6
# in Thread1 got 7
# in Thread1 got 8
# in Thread1 got 9
# in Thread1 got 10
# in Thread1 got 11
# in Thread1 got 12
# in Thread1 got 13
# in Thread1 got 14
# in Thread1 got 15
# in Thread1 got 16
# in Thread1 got 17
# in Thread1 got 18
# in Thread1 got 19
# main done