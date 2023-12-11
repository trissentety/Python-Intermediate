#Class decorator
#Typical use cases:
#Timer decorator - Calculate execution time of func
#Debug decorator - Print out more information about called function and it's arguments
#Check decorator - Check if arguments fulfull some requirements and depth of the behavior
#Register functions - Plugins
#Cache return values
#Add information
#Update state
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        self.num_calls += 1
        print(f'This is execuuted {self.num_calls} times')
        return self.func(*args, **kwargs)



@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello():
    print("Hello!")

say_hello()
# This is execuuted 1 times
# Hello!
say_hello() #multiple executions
# This is execuuted 2 times
# Hello!