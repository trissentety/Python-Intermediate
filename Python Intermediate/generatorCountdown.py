#countdown generator
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4) #num

value = next(cd) #starts from beginning of func and executes it returns Starting only
print(value) #prints 4

print(next(cd)) #does loop twice 
# Starting
# 4
# 3

print(next(cd)) #2
print(next(cd)) #1
print(next(cd)) #stop iteration