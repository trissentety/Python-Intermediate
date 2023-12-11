#Class decorator
import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        functools.update_wrapper(self, func)
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)
# Call 1 of 'say_hello'
# Hello!
# Call 2 of 'say_hello'
# Hello!