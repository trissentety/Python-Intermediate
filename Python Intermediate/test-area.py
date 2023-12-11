def start_end_decorator(func): #decorator function
    
    def wrapper(): #wraps function
        print('Start') #extending behavior by doing something before and after
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
    
print_name() #Alex

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name) #print name now has decorator function
print_name()