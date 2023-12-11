#decorators with arguments
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func) #decorator
        def wrapper(*args, **kwargs):
            for _ in range(num_times): #repeat number of times given
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3) #decorator repeat 3 times
def greet(name):
    print(f"Hello {name}")
    
greet('Alex')