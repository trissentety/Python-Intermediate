from multiprocessing import Process
import os
import time


def square_numbers(): #target example for processes
    for i in range(1000):
        result = i * i
        time.sleep(0.1) #see task manager processes when executed to see process run


processes = [] #store processes
num_processes = os.cpu_count() #numper of cpu's on machine best practice

# create processes and asign a function for each process
for i in range(num_processes):
    process = Process(target=square_numbers) #target is callable function executed by this program, if args, args tuple ,args=()
    processes.append(process) #add

# start all processes
for process in processes:
    process.start()

# wait for all processes to finish
# block the main thread until these processes are finished
for process in processes:
    process.join()

print('end main') #only when all processes are done