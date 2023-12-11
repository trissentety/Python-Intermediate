# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.

#extends behavior of function without modifying it
#python are first class objects meaning they can be defined in another function, passed as an argument to another func, and returned from other function
def start_end_decorator(func): #decorator function
    
    def wrapper(): #wraps function
        print('Start') #extending behavior by doing something before and after
        func() #print name function
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')
    
print_name() #Alex

print()

print_name()
# Start
# Alex
# End