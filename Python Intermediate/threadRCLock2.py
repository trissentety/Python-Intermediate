from threading import Thread, Lock
import time

database_value = 0 #simulate db

def increase(lock): #give lock given in args 
    global database_value #in order to modify global variable below
    with lock:#recommeneded way to use locks as a context manager
        #database access
        local_copy = database_value #beginning 0

        #processing
        local_copy += 1 #modify copy
        time.sleep(0.1) #intelligently switch to next thread from waiting time
        database_value = local_copy #write new value back into database when done, switches back to thread 1 from sleeping thread 2
        
if __name__ == "__main__":
    lock = Lock() #create Lock

    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock,)) #comma so python knows its a tuple
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()

    thread1.join() #wait for threads to complete
    thread2.join()

    print('end value', database_value)
    print('end main')


# start value 0
# end value 2
# end main
