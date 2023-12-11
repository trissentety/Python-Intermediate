def start_end_decorator(func): #decorator function
    
    def wrapper(*args, **kwargs): #wraps function. requires same arguments as func provided, *args, **kwargs to use as many arguments and keyword arguments as necessary
        print('Start') #extending behavior by doing something before and after
        result = func(*args, **kwargs) #print name function, no result prints None
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
# Start
# End
# 15