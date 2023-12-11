#Class decorator
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        print('Hi there')

cc = CountCalls(None) #object of class
cc() #execute as function

@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello():
    print("Hello!")
#Hi there
