def mygenerator():
    yield 1 #stops and returns 1 after one execution
    yield 2
    yield 3

# g = mygenerator()
# print(g) #<generator object mygenerator at 0x000001188A68AB90>

# g = mygenerator()
# for i in g:
#     print(i)
# 1
# 2
# 3

g = mygenerator()
value = next(g)
print(value)
# 1

value = next(g)
print(value)
# 2

value = next(g)
print(value)
# 3

value = next(g)
print(value)
# traceback StopIteration