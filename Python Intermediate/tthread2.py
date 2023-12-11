from threading import Thread
import time

database_value = 0 #simulate db

def increase(): #thread 2 starts from wait time, database value is still 0 at time
    global database_value #in order to modify global variable below
    #database access
    database_value = local_copy #beginning 0

    #processing
    local_copy += 1 #modify copy
    time.sleep(0.1) #intelligently switch to next thread from waiting time
    database_value = local_copy #write new value back into database when done, switches back to thread 1 from sleeping thread 2
        
if __name__ == "__main__":
    print('start value', database_value)
    thread1 = Thread(target=increase) #create thread
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()

    thread1.join() #wait for threads to complete
    thread2.join()

    print('end value', database_value)
    print('end main')

    #value of 1 because of race condition happening when two or more threads try to modify same variable at same time
    #start value 0
    #end value 1
    #end main
