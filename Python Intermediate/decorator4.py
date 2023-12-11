import functools

#Decorator identity function
def start_end_decorator(func): #decorator function
    @functools.wraps(func) #reserves information of used function
    def wrapper(*args, **kwargs): #wraps function. requires same arguments as func provided, *args, **kwargs to use as many arguments and keyword arguments as necessary
        print('Start') #extending behavior by doing something before and after
        result = func(*args, **kwargs) #print name function, no result prints None, inner function within an inner function
        print('End') #doing something after
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

#exclude this for template for decorator function
print(help(add5))
print(add5.__name__)
