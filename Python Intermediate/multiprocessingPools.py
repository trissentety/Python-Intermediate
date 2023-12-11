from multiprocessing import Pool 
#controls a pool of worker processes to which chops can be submitted
#manage available processes and split
#example data into smaller chunks which can then be processed in parallel by different processes
#takes care of a lot of stuff
#four important methods - map, apply, join, close 

def cube(number): #function is executed and paralleled by difference processes
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool() #create pool

    # by default this allocates the maximum number of available 
    # processors for this task --> os.cpu_count()
    #submits iterable into byte sized chunks and submit to function
    result = p.map(cube,  numbers) #automatically allocate num of processes and create different processes, as many processes as cores on machine
    pool.apply(cube, numbers[1])#have 1 function executed by pool. execute process with 1 argument


    # or 
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close() #wait for pool to process all calculations and return result
    p.join()
    
    print(result)

    # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] #cubed
