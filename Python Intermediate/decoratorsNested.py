# a decorator function that prints debug information about the wrapped function
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper



def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #arguments, keyword arguments
        args_repr = [repr(a) for a in args] #extracts name
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})") #prints information of function
        result = func(*args, **kwargs) #executes function
        print(f"{func.__name__!r} returned {result!r}") #prints information about return value, 'say_hello' returned 'Hello Alex'
        return result
    return wrapper

#multiple decorators executed in order listed
@debug
@start_end_decorator
def say_hello(name): #insede start end decorator executes say hello function
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')
# Start
# Hello Alex
# End
# 'say_hello' returned 'Hello Alex'