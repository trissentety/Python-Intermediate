import sys
# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0) #puts elements in generator object
#iterates each number on new line
print(sys.getsizeof(mygenerator)) #208

#convert object to list
print(list(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist)) #4216
#adds numbers to list even

