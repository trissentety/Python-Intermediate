#Generators are functions that return a opbject that can be iterated over
#generate items inside object lazily, generates items one at a time only when you ask for it
#more memory efficient that other sequence objects when you have to deal with large datasets
#powerful advanced python technique
#defined like normal function but with yield keyword instead of return keyword
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration
print(next(cd))