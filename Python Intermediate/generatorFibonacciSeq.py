#generator fibonacci
# 0 1 and all following numbers are sum of previous 2 numbers (0 + 1 = 1) (1 + 1 = 2) (1 + 2 = 3) 5 8 13 etc

def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))
# [0, 1, 1, 2, 3, 5, 8, 13, 21]