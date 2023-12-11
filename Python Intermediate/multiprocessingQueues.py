# import Lock
from multiprocessing import Lock
from multiprocessing import Process, Value, Array
from multiprocessing import Queue #linear data structure
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i) #calculate square and put it in numbers

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q,))

p1.start()
p2.start()

p1.join()
p2.join()

while not q.empty():
    print(q.get()) #return and remove first element in queue

# -1
# -2
# -3
# -4
# -5
# 1
# 4
# 9
# 16
# 25
