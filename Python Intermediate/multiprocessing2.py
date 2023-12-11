from multiprocessing import Process, Value, Array, #lock #special shared memeory objects array and value
import time

def add_100(number): #lock
    for _ in range(100):
        time.sleep(0.01)
        #lock.acquire()
        number.value += 1
        #lock.release()

def add_100_array(numbers):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1


if __name__ == "__main__":

    #lock = lock()
    shared_number = Value('i', 0) #takes 2 args
    print('Value at beginning:', shared_number.value) #0

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number,)) #lock
    process2 = Process(target=add_100, args=(shared_number,)) #lock

    process3 = Process(target=add_100_array, args=(shared_array,)) #lock
    process4 = Process(target=add_100_array, args=(shared_array,)) #lock

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')

# Value at beginning: 0
# Array at beginning: [0.0, 100.0, 200.0]
# Value at end: 200
# Array at end: [199.0, 300.0, 400.0]
# end main