import sys
#generator large data
#don't have to wait for all elements to be generated before starting to use them
#example get very first item first next statement and don't have to calculate all numbers
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# myList = firstn(10)
# print(firstn(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(sum(firstn(10)))
# 45

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10))) #same result 45

# print(sys.getsizeof(firstn(10))) #184
# print(sys.getsizeof(firstn_generator(10))) #200

print(sys.getsizeof(firstn(1000000))) #8697464
print(sys.getsizeof(firstn_generator(1000000))) #120

