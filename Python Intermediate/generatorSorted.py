#Generator sorted
def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()

print(sorted(g))
#[1, 2, 3]