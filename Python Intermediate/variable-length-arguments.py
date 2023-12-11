#*args pass any number of positional arguments to function
#**kwargs pass any number of keyword arguments to function. 
#name whatever example *a, **k
def foo(a, b, *args, **kwargs): #args kwargs is tuple inside function
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
foo(1, 2, three=3)
