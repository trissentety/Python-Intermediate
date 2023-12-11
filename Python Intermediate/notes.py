#Copy list (ordered mutable)
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
#or
list_cpy = list(list_org)
#or
list_cpy = list_org[:]

#Square numbers in list
mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist] #expression and for in loop

#Tuple is collection datatype ordered immutable. Tuple can't be changed after creation
mytuple = "Max", 28, "Boston" #parentheses are optional. if only 1 value in tuple then needs a comma at the end otherwise string
#function to create tuple
mytuple = tuple(["Max", 28, "Boston"])

item = mytuple[0]
#iterate tuple
# for i in mytuple:
#     print(i)

# if "Max" in mytuple:
    # print("yes")
# else:
    # print("no")

#print(mytuple.count("p") #returns number of elements in tuple
#print(mytuple.index("p")) #returns first occurrence of element









my_tuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple

print(i1)
print(i3)
print(i2)

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes") #104 bytes cause list
print(sys.getsizeof(my_list), "bytes") #88 bytes cause tuple


import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) #create list 1,000,000 times and see how long it takes to make it #0.169 
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) #0.019 9 times faster~ for tuple


#Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston") #no quotes for keys
print(mydict2)

value = mydict["name"] #prints key's value
print(value)

mydict["email"] = "max@xyz.com" #add item
print(mydict)

mydict["email"] = "coolmax@xyz.com" #updates to coolmax@xyz.com
print(mydict)

del mydict["name"]
print(mydict)

mydict.popitem() #removes last item .pop("age") to remove specific item
print(mydict)

if "name" in mydict:
    print(mydict["name"]) #prints Max

try:
    print(mydict["name"])
except:
    print("Error")

for key in mydict.keys():
    print(key) #prints all keys on new line each

for key in mydict.keys():
    print(key) #same thing

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict2 = mydict #not real copy because it updates the value in memory
mydict2 = mydict.copy() #copy
mydict2= dict(mydict) #copy

mydict = {"name": "Max", "age": 28, "email":"max@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict2)
#prints {'name': 'Mary', 'age': 27, 'email':'max@xyz.com', 'city': 'Boston}

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
#{3: 9, 6: 36, 9: 81}
value = my_dict[0]
9

mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)

#Sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset) #{1, 2, 3}
myset = set([1, 2, 3])
myset = set("Hello") print {'o', 'l', 'H', 'e'} #makes it load faster?

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3) #key error if number not found
myset.discarc(3) #no key error
myset.clear() #empties set
myset.pop() #returns and removes value print(myset.pop())

print(myset)

for i in myset:
    print(i)

if 1 in myset:
    print("yes")

#union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) #combines numbers from 2 sets without duplication
print(u) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens) #only elements in both sets
print(i) #nothing because both sets don't have same elements at all

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff) #{4, 5, 6, 7, 8, 9} numbers from first set that are not in second set
diff = setB.difference(setA) #{10, 11, 12}

diff = setB.symmetric_difference(setA) #all elements from set a and b but not elements that are in both sets

setA.update(setB) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(setA) #updates set with elements found in other set not duplicates

setA.difference_update(setB) #{4, 5, 6, 7, 8, 9} updates set by removing elements found in other set

setA.symmetric_difference_update(setB) #Only keeps elements found in setA and in setB but not elements found in both
#{4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB)) #False 1,2,3,4,5,6 is not in setB
print(setB.issubset(setA)) #True 1,2,3 is also in setA
print(setB.issuperset(setA)) #if first set contains all numbers of second set. opposite of issubset
print(setA.isdisjoint(setB)) #returns True if both sections have a null intersection so no same elements, False same elements
setC = {7, 8}
print(setA.indisjoint(setC)) #True have totally different elements

setB = setA.copy() #copy method
setB = set(setA) #copy
print(setB)

a = frozenset([1, 2, 3, 4]) #immutable copy version of normal set
a.add(2) #error .remove(2) error

print(a)

#Strings: ordered, immutable, text representation
my_string = 'Hello world'
print(my_string)
my_string = """Hello World""" #goes over multiple lines or single line
my_string = """Hello \ #no new line
 World"""

my_string = "Hello World"
char = my_string[0] #first character
print(char) 

substring = my_string[1:5] #ello
substring = my_string[:5]#hello
substring = my_string[:] #Whole string
substring = my_string[::1] #same thing
print(substring)
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name

for i in greeting:
    print(i) #iterates new line each character

my_string.strip() #removes white space around string
my_string.upper() #uppercase
my_string.lower() #lower
my_string.startswith("H") #True
my_string.startswith("World") #False
my_string.endswith("World") #True
print(my_string.find('lo')) #index 3, -1 no find
my_string.count('p') #0, o has 2

#mutable confusion, confuses Patrick
my_string.replace('World', 'Universe') #Hello Universe

my_string = 'how are you doing'
my_list = my_string.split() #each word as element in list, delimiter default, 'how,are,you,doing (",")
print(my_list) #['how', 'are', 'you', 'doing']

new_string = ''.join(my_list) #convert list back to string
print(new_string) #howareyoudoing
new_string = ' '.join(my_list) #how are you doing

my_list = ['a'] * 6 #create list with six a elements
my_string = ''

for i in my_list: #bad creates new string and assigns back to original string expensive
    my_string += i 

my_string = ''.join(my_list) #good cleaner and faster
print(my_string)

from timeit import default_timer as timer

start = timer()
my_string = ''
for i in my_list: #bad creates new string and assigns back to original string expensive
    my_string += i 
stop = timer()
print(stop-start) #6.46

start = timer()
my_string = ''.join(my_list) #good cleaner and faster
print(my_string)
print(stop-start) #2.72

#Formatting strings
# %, .format(), f-Strings (new method)
var = "Tom"
my_string = 'the variable is %s' % var #first method tells interpreter there's a placeholder with string and fill placeholder with var

var = 3
my_string = 'the variable is %d' % var #if digit used
print(my_string)

var = 3.1234567
my_string = "the variable is %f" % var #if floating point used
print(my_string)

my_string = "the variable is {:.2f}".format(var)
my_string = "the variable is %.2f" % var #fixed floating point
my_string = "the variable is {:.2f}".format(var) #fixed floating point
var2 = 6
#Multiple variables
my_string = "the variable is {:.2f} and {}".format(var,var2) #fixed floating point
print(my_string)

my_string = f"the variable is {var} and {var2}"
print(my_string)

my_string = f"the variable is {var * 2} and {var2}" #math on variable

#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) #Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items()) #dict_keys([('a' 5), ('b', 4), ('c', 3)])
print(my_counter.keys()) #dict_keys(['a', 'b', 'c'])
print(my_counter.values()) #dict_keys([5, 4, 3])

print(my_counter.most_common(1)) #most common item by count [('a', 5)]
print(my_counter.most_common(2)) #most common item by count [('a', 5), ('b', 4)]

print(my_counter.most_common(1)[0][0]) #a, [0]index 0 [0]element

print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', ]

from collections import namedtuple
Point = namedtuple('Point', 'x, y') #class point with fields x and y, Point is name of namedtuple
pt = Point(1, -4)
print(pt) #Point(x=1, y=-4)
print(pt.x, pt.y) #1 -4


from collections import OrderedDict #like regular dictionary but rememebers the order items are inserted
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) #OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#newer versions of python remembers order
ordered_dict = {}

from collections import defaultdict #has a default value if key isn't set, by default 0
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d) #defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) #1
print(d['c']) #0 default value
d = defaultdict(float) #0.0

from collections import deque #double ended queue used to add or remove elements from either end
d = deque()

d.append(1)
d.append(2)
print(d) #deque([1, 2])

d.appendleft(3) #deque([3, 1, 2])
print(d)

d.pop()
print(d) #deque([3, 1])
d.popleft() #deque([1, 2])
d.clear #deque([])
d.extend([4,5,6]) #dque([3, 1, 2, 4, 5, 6])
d.extendleft([4,5,6]) #dque([6, 5, 4, 3, 1, 2,])
d.rotate(1) #deque([2, 6, 5, 4, 3, 1])
d.rotate(2) #deque([1, 2, 6, 5, 4, 3])
d.rotate(-1) #deque([5, 4, 3, 1, 2, 6]) #rotate left

#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod) #<intertools.product object at 0x1045fa630
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)] #combins them


a = [1, 2]
b = [3]
prod = product(a,b, repeat=2) #product computes Catesian product of the input iterables
#[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

from itertools import permuatations #returns all possible orderings of an input
a = [1, 2, 3]
perm = permutations(a) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(perm)) 

perm = permutations(a, 2) #length of 2 posbbilities [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from intertools import commbinations #make all combos with specified length
a = [1, 2, 3, 4]
comb = combinations(a, 2) #[(1, 2), (1, 3), (2, 4), (2, 3), (2, 4), (3, 4)]
print(list(comb))

from itertools import combinations, combinations_with_replacement #uses combos of itself as well (1, 1)
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) #[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print(list(comb_wr)) 

from itertools import accumulate #makes iterator that returns accumulated sums, or any other binary function
acc = accumulate(a) [1, 3, 6, 10]
print(a)
print(list(acc))

from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul) #[1, 2, 6, 24] 1* 2 = 2, 2*3=6, 6*4=24
print(a)
print(list(acc)) 
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max) #[1, 2, 5, 5, 5] iterates a new max

from itertools import groupby #makes an iterator that returns keys and groups from an iterable
def smaller_than_3(x) :
    return x < 3 #True or False
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) #iterates groups smaller than three returns true false
print(group_obj) #<itertools.groupby object at 0x110032d58>
for key, value in group_obj:
    print(key, list(value))
#True [1, 2]
#False [3, 4]

group_obj = groupby(a, key=lambda x: x < 3) #does same thing #small one line functions with input will do some expression and return output

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age']) #groups by age
for key, value in group_obj:
    print(key, list(value))
#25 [{'name': 'Tim', 'age':25}, {'name': 'Dan', 'age': 25}]
#27 [{'name': 'Lisa', 'age':27}
#28 [{'name': 'Claire', 'age':28}

from itertools import count, cycle, repeat
for i in count(10): #starts at 10 prints infinite loop each iteration and adds 1
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i) #1 new line 2 new line 3 new line 1 new line 2 new line 3 new line infinitely

for i in repeat(1): #infinite print 1
    print(i)
for i in repeat(1, 4): #repeats 1 four times

# lambda arguments: expression
#creates function with arguments, evaluates expression and returns results

add10 = lambda x: x + 10
print(add10(5)) #returns 15

def add10_func(x): #same as
    return x + 10

mult = lambda x,y: x*y
print(mult(2, 7)) #14
#typically used for simple function used only once in code
#or as argument to higher order functions that take in orther functions as arguments
#example they're used along with built in functions sorted, map, filter and reduce

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)#[(1, 2), (5, -1), (10, 4), (10, 4)] #default sorts by first argument

print(points2D)
print(points2D_sorted) 
points2D_sorted = sorted(points2D, key=lambda x: x[1])#[(5, -1), (15, 1), (1, 2), (10, 4)] #sorts by second index

def sort_by_y(x):
    return x[1]

points2D_sorted = sorted(points2D, key=sort_by_y) #same thing second index

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) # [(1, 2), (5, -1), (10, 4), (15, 1)] sorts according to sum of each tuple

#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a) #each element multiplied by 2 [2, 4, 6, 8, 10]
print(list(b)) 

c = [x*2 for x in a] #does same thing same results, easier
print(c)

#Filter function
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a) #[2, 4, 6]
print(list(b)) 

c = [x for x in a if x%2==0] #same #[2, 4, 6]
print(c)

from functools import reduce
#reduce (func, seq)
a = [1, 2, 3, 4] # 24 1*2=2,2*3=6,6*4=24
product_a = reduce(lambda x,y: x*y, a) #a is sequence
print(product_a)


#Exceptions
#Errors and Exceptions
a = 5
print(a)) #syntax error
a = 5 + '10' #type error
import somemodule #module not found error

a = 5
b = c #name error c is not defined

f = open('somefile.txt') #file not found error no such file or directory

a = [1,2,3]
a.remove(4) #ValueError list.remove(x): x not in list
print(a) 

a = [1, 2, 3]
a[4]
print(a)

my_dict = {'name': 'Max'}
my_dict['age'] #KeyError: 'age' 

#Exception Errors
x = -5
if x < 0:
    raise Exception('x should be positive') #AssertionError: x is not positive

#Catch exceptions with try except blocks
try:
    a = 5 / 0 #normally raises ZeroDivisionError
except:
    print('an error happened') #an error happened

try:
    a = 5 / 0 #normally raises ZeroDivisionError
except Exception as e:
    print('e') #division by zero prints error message from zero divison class

try:
    a = 5 / 0
    b = a + '10' #multiple tests
    b = a + 4 #multiple tests
except ZeroDivisionError as e:
    print(e)
except TypeError as e: #unsupported operrand types(s) for x: 'float' and 'str'
    print(e)
else: #if everything went fine 
    print('everything is fine')
finally: #always runs no matter if there was exception or not
    print('cleaning up...')

#Define own exceptions and error classes
class ValueTooHighError(Exception) : #typically class with name and error at end, base class Exception class
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


test_value(200) #__main__.ValueTooHighError('value is too high')


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(1)
except ValueTooHighError as e:
    print(e) #value is too high
except ValueTooSmallError as e:
    print(e.message, e.value) #value is too small 1


import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', #format specify LogRecord attributes, logs time, level name and actual message
    datefmt='%m/%d/%Y %H:%M:%S') #specifying how the time should be logged
#by default name root logger
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')
#by default only message with level warning or above are printed
# WARNING:root:This is a warning message
# ERROR:root:This is a error message
# CRITICAL:root:This is a critical message

# 12/05/2023 05:49:51 - root - DEBUG - This is a debug message
# 12/05/2023 05:49:51 - root - INFO - This is a info message
# 12/05/2023 05:49:51 - root - WARNING - This is a warning message
# 12/05/2023 05:49:51 - root - ERROR - This is a error message
# 12/05/2023 05:49:51 - root - CRITICAL - This is a critical message


#Create logger
import logging

logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Configure level and formatter and add it to handlers
stream_handler.setLevel(logging.WARNING) # warning and above is logged to the stream
file_handler.setLevel(logging.ERROR) # error and above is logged to a file

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error') # logged to the stream AND the file!

#2023-12-05 06:40:45,866 - __main__ - ERROR - This is an error

#logging.config
#using the file config or dict config method



#logging.config
#using the file config or dict config method
# logging.conf
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s


import logging
try:
    a = [1,2,3] #list with values
    val = a[4] #access value with index value too large
except IndexError as e: #catch with except error
    # logging.error(e) #default logs error message with index out of range
#ERROR:root:list index out of range

#to also log stack trace:
    logging.error(e, exc_info=True)
#ERROR:root:list index out of range
# Traceback (most recent call last):
#   File "c:\Users\triss\Desktop\python3\Python Intermediate\main.py", line 19, in <module>
#     val = a[4] #access value with index value too large
#           ~^^^
# IndexError: list index out of range


#same as above alt
import logging
import traceback
try:
    a = [1,2,3] #list with values
    val = a[4] #access value with index value too large
except: #catch with except error
    logging.error("The error is %s", traceback.format_exec()) #string formatting does same thing includes traceback


#rotating file handlers
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__) #Create logger
logger.setLevel(logging.INFO) #Set level

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) #Create file handler, name of file, max bytes (2kb), keep five backup counts
logger.addHandler(handler) #add handler to logger

for _ in range(10000): #log many messages, underscore means no care
    logger.info('Hello, world!') #log hello world
    #Makes different log files all with hello world message
    #Inside folder each file is 2kb and after 2kb it gets rolled over


import logging
import time
from logging.handlers import TimedRotatingFileHandler #creates a rotating lock based on how much time is passed
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0 (monday), w1 (tuesday)
# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5) #when rotate every, at interval 5, backup of 5 files
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(5) #import time sleep seconds

#creates new files named timed_test.log.2023-12-05_07-53-36

#if there's a lot of different modules and log many different things especially if using microservice architecture then not recommended to use log but use JSON format for logging
#recommended to use open source python-json-logger from madzak


import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


#JSON (Javascript Object Notation) - Lightweight data format that is used for data exchange. Heavily used in web applications. 
#Python comes with build in JS module that makes JSON data very easy to handle. similar to dict with key value pairs
#Encode decode json with module
#Values can take strings, numbers, Booleans, nested types ex nested array, nested dictionary
#python-engineer.com for conversion table

{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": [
        "running",
        "swimming",
        "singing"
    ],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}

#How python is traslated to JSON and vice versa
# Python	JSON
# dict	object
# list, tuple	array
# str	string
# int, long, float	number
# True	true
# False	false
# None	null 

# import json

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# # convert into JSON:
# person_json = json.dumps(person)
# # use different formatting style
# person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# # the result is a JSON string:
# print(person_json) 
# print(person_json2) 


import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person) #dumps object to json string (know cause false is now lowercase)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True) #indent makes json display nicer, seperators change "name": "John", to "name"= "John"; Not recommended. sort_keys argument sorts keys alphabetically
# the result is a JSON string:
print(person_json) 
print(person_json2) 

with open('person.json', 'w') as file: #dump file into person.json, open in write mode, JSON.dump
    json.dump(person, file, indent=4) #dump person object into file

# {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }


#convert json back to python dictionary
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person) #dumps object to json string (know cause false is now lowercase)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True) #indent makes json display nicer, seperators change "name": "John", to "name"= "John"; Not recommended. sort_keys argument sorts keys alphabetically
# the result is a JSON string:
print(person_json) 
print(person_json2) 

# {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }

#converting JSON back to python object/dictionary called deserialization or decoding
person = json.loads #load from a string
print(person) #python dictionary cause false is now False


import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person) #dumps object to json string (know cause false is now lowercase)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True) #indent makes json display nicer, seperators change "name": "John", to "name"= "John"; Not recommended. sort_keys argument sorts keys alphabetically
# the result is a JSON string:
print(person_json) 
print(person_json2) 
#converting to JSON file does same thing, decoding json data
with open('person.json', 'r') as file: #dump file into person.json, open in write mode, JSON.dump
    person = json.load(file) #load from a string
    print(person) #python dictionary cause false is now False
#{'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

#How to encode custom object
import json
class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')
userJSON = json.dumps(user, default=encode_user) #error if not serialized,  default method, encode user func uses encode_user for how to encode object
print(userJSON) #{"name": "Max", "age": 27, "User": true}


#Does same thing as above
import json

class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')

#Implement custom JSON encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    #override default method encode_user
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        #otherwise let base json encoder handle it
        return JSONEncoder.default(self, o)
userJSON = json.dumps(user, cls=UserEncoder) #class argument as class with UserEncoder
print(userJSON) #{"name": "Max", "age": 27, "User": true}


#Alternative to same thing as above ending for encoding custom object
import json

class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')

#Implement custom JSON encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    #override default method encode_user
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        #otherwise let base json encoder handle it
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user) #class argument as class with UserEncoder
print(userJSON) #{"name": "Max", "age": 27, "User": true}


#Decode custom object back to python dict
import json

class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')

#Implement custom JSON encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    #override default method encode_user
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        #otherwise let base json encoder handle it
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user) #class argument as class with UserEncoder
print(userJSON) #{"name": "Max", "age": 27, "User": true}

#Decode object back, user json format converted back to normal python object
user = json.loads(userJSON)
print(user) #print(type(user)) <class 'dict'>
# {"name": "Max", "age": 27, "User": true}
# {'name': 'Max', 'age': 27, 'User': True}


import json

class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')

#Implement custom JSON encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    #override default method encode_user
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        #otherwise let base json encoder handle it
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user) #class argument as class with UserEncoder
print(userJSON) #{"name": "Max", "age": 27, "User": true}

#decode into user object by writing custom decoding method
def decode_user(dct):
    if User.__name__ in dct: #checks if dictionary contains a user key, in encod_user func added class as key
        #then create and return user object
        return User(name=dct['name'], age=dct['age']) #gets name from dict, dict with key name, age of dict
    #otherwise returns dict
    return dict

#Decode object back, user json format converted back to normal python object
user = json.loads(userJSON, object_hook=decode_user) #method object_hook set to decoding message
print(type(user))
print(user) #print(type(user)) <class 'dict'>
# {"name": "Max", "age": 27, "User": true}
# {'name': 'Max', 'age': 27, 'User': True}


#Python Random
#random module for sudo random numbers, 
#secrets module for cryptographically strong random numbers, 
#NumPy random to generate arrays with random numbbers
import random
#pseudo distribution because numbers seem random but are reproducible
# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b] (0-10)
a = random.uniform(1,10)
print(a)

# random integer in range [a,b]. b is included, random range 1 to 10
a = random.randint(1,10)
print(a)

# random integer in range [a,b). b is excluded, Same thing as above but doesn't include 10
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma, useful if working with statistics (0 to 0.5)
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence, 3 of them
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list, same thing as above but not unique
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle whole list in place random order 
a = list("ABCDEFGHI") #['B', 'C', 'G', 'D', 'E', 'A', 'H', 'F']
random.shuffle(a)
print(a)


#Random seeding
import random

print('Seeding with 1...\n')
#reproduces random numbers. Not recommended for security purposes
random.seed(1)
print(random.randint(1,10))
print(random.random())
# 0.13436424411240122
# 2
#Same values when this runs again
random.seed(1)
print(random.randint(1,10))
print(random.random())
# 0.13436424411240122
# 2
# 0.13436424411240122
# 2

import random
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2) #makes new random numbers but is similar to above 
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
# 0.13436424411240122
# 2
# 0.9560342718892494
# 1
# 0.13436424411240122
# 2
# 0.9560342718892494
# 1

print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))
# Seeding with 1...

# 0.13436424411240122
# 8.626903632435095
# B

# Re-seeding with 42...

# 0.6394267984578837
# 1.2250967970040025
# E

# Re-seeding with 1...

# 0.13436424411240122
# 8.626903632435095
# B

# Re-seeding with 42...

# 0.6394267984578837
# 1.2250967970040025
# E


#Random secrets 
import secrets #more secure and truly random. 
#Useful fore passwords, security tokens, account authentication
#takes more time to generate

# random integer in range [0, n), exclusive upper bound, 0 to 10 and 10 is not included
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits, random binary values by amount provided
a = secrets.randbits(4) #1111 (2*2*2 + 2*2 + 2 + 1), 0 Up to 15 included
print(a)
#each run
#4
#10
#2
#7
#5

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI")) #Random choice not reproducable
print(a)


import numpy as np

a = np.random.rand()



#numpy random
import numpy as np #typical
#uses different random generator and seed function than python's built in module

np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)

print(np.random.rand(3)) #1d array with 3 random float elements
#[0.62027501 0.87129171 0.89059522]
# reset the seed
np.random.seed(1)
print(np.random.rand(3))

# generate nd array with random integers in range [a,b) with size n
values = np.random.randint(0, 10, (5,3)) #0 to 10 and 10 not included, size 3 1d array or tuple with more dimensions
print(values)
# values = np.random.randint(0, 10, (5,3))
# [[8 8 9]
#  [0 8 5]
#  [6 4 3]
#  [2 3 1]
#  [9 0 5]]
# values = np.random.randint(0, 10, 3)
# [5 7 5]


# generate nd array with Gaussian values, array has size (d0,d1,…,dn)
# values from standard normal distribution with mean 0.0 and standard deviation 1.0
values = np.random.randn(5)
print(values)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)
#  [[7 8 9]
#  [4 5 6]
#  [1 2 3]]

#use this one instead of python's built method
np.random.seed(1)
print(np.random.rand(3,3))
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]


#Decorator functions
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

def print_name():
    print('Alex')
    
print_name() #Alex

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name) #print name now has decorator function
print_name()
# Alex

# Start
# Alex
# End


#Does same thing as above by using start_end_decorator this time
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


#decorator using arguments
def start_end_decorator(func): #decorator function
    
    def wrapper(*args, **kwargs): #wraps function. requires same arguments as func provided, *args, **kwargs to use as many arguments and keyword arguments as necessary
        print('Start') #extending behavior by doing something before and after
        result = func(*args, **kwargs) #print name function, no result prints None
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
# Start
# End
# 15


#Decorator identity function
import functools

def start_end_decorator(func): #decorator function
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #wraps function. requires same arguments as func provided, *args, **kwargs to use as many arguments and keyword arguments as necessary
        print('Start') #extending behavior by doing something before and after
        result = func(*args, **kwargs) #print name function, no result prints None
        print('End') #doing something after
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

#exclude this for template for decorator function
print(help(add5))
print(add5.__name__)


#decorators with arguments
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func) #decorator
        def wrapper(*args, **kwargs):
            for _ in range(num_times): #repeat number of times given
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3) #decorator repeat 3 times
def greet(name):
    print(f"Hello {name}")
    
greet('Alex')


#Nested decorators
# a decorator function that prints debug information about the wrapped function
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #arguments, keyword arguments
        args_repr = [repr(a) for a in args] #extracts name
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})") #prints information of function
        result = func(*args, **kwargs) #executes function
        print(f"{func.__name__!r} returned {result!r}") #prints information about return value
        return result
    return wrapper

#multiple decorators executed in order listed
@debug
@start_end_decorator
def say_hello(name): #insede start end decorator executes say hello function
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')
# Start
# Hello Alex
# End
# 'say_hello' returned 'Hello Alex'


#Class decorator
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        print('Hi there')

cc = CountCalls(None) #object of class
cc() #execute as function

@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello():
    print("Hello!")
#Hi there


#Class decorator simple
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        print('Hi there')

cc = CountCalls(None) #object of class
cc() #execute as function

@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello():
    print("Hello!")
#Hi there


#Decorator class num times
#Class decorator
#Typical use cases:
#Timer decorator - Calculate execution time of func
#Debug decorator - Print out more information about called function and it's arguments
#Check decorator - Check if arguments fulfull some requirements and depth of the behavior
#Register functions - Plugins
#Cache return values
#Add information
#Update state
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        self.num_calls += 1
        print(f'This is execuuted {self.num_calls} times')
        return self.func(*args, **kwargs)



@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello():
    print("Hello!")

say_hello()
# This is execuuted 1 times
# Hello!
say_hello() #multiple executions
# This is execuuted 2 times
# Hello!


#Say hello decorator class
#Class decorator
import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func): #similar to decorator function
        functools.update_wrapper(self, func)
        self.func = func #save as class variable
        self.num_calls = 0 #state. keeps track of how many times executed
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs): #to implement class decorator
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls #class decorator, does same thing as fuc decorators typically used to maintain and upate a state
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)
# Call 1 of 'say_hello'
# Hello!
# Call 2 of 'say_hello'
# Hello!


#Generators
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


#Generator simple
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


#Generator sum
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

print(sum(g))


#Generator sorted
def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()

print(sorted(g))
#[1, 2, 3]


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


#generator large data
import sys
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


#generate fibonacci sequence
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


# generator expression
import sys
mygenerator = (i for i in range(1000) if i % 2 == 0) #puts elements in generator object
#iterates each number on new line
print(sys.getsizeof(mygenerator)) #208

#convert object to list
print(list(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist)) #4216
#adds numbers to list even


# A Process is an instance of a program, e.g. a Python interpreter. They are independent from each other and do not share the same memory.

# Key facts:

# A new process is started independently from the first process

# Takes advantage of multiple CPUs and cores

# Separate memory space

# Memory is not shared between processes

# One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation - Global interpreter log

# Great for CPU-bound processing

# Child processes are interruptable/killable

# Starting a process is slower that starting a thread

# Larger memory footprint

# IPC (inter-process communication) is more complicated

# Threads
# A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

# Key facts:

# Multiple threads can be spawned within one process

# Memory is shared between all threads

# Starting a thread is faster than starting a process

# Great for I/O-bound tasks - input output tasks
#if process is slow can intelligently switch to other threads and do processing in meantime like network connection 

# Leightweight - low memory footprint

# One GIL for all threads, i.e. threads are limited by GIL

# Multithreading has no effect for CPU-bound tasks due to the GIL

# Not interruptible/killable -> be careful with memory leaks

# increased potential for race conditions - two or more threads want to modify same variable at same time causes bugs and crashes

# Threading in Python
# Use the threading module.

# Note: The following example usually won't benefit from multiple threads since it is CPU-bound. It should just show the example of how to use threads.

#thread is entity of process


#GIL: Global interpreter lock
# A lock that allows only one thread ata time to execute in Python
#Needed in CPython because memory management in not thread safe

#Avoic
#Use multiprocessing
#Use a different, free-threaded Python implementation (Jython, IronPython)
#Use python as a wrapper for third-party libraries (C/C++) => numpy, scipy

#Python has reference variable to keep track of number of references that point to object. When this count reaches 0, memory occupied by the object can be released
#This reference count variable needs protection from race conditions where two threads increase or decrease the value simulataneously.
#Could cause leaked memory, incorrectly release memory while reference to that object still exists


#multiprocessing
from multiprocessing import Process
import os
import time


def square_numbers(): #target example for processes
    for i in range(1000):
        result = i * i
        time.sleep(0.1) #see task manager processes when executed to see process run


if __name__ == "__main__":
    processes = [] #store processes
    num_processes = os.cpu_count() #numper of cpu's on machine best practice

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers) #target is callable function executed by this program, if args, args tuple ,args=()
        processes.append(process) #add

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()

    # print('end main') only when all processes are done


    #multiprocessing 2
    from multiprocessing import Process
import os
import time


def square_numbers(): #target example for processes
    for i in range(1000):
        result = i * i
        time.sleep(0.1) #see task manager processes when executed to see process run


processes = [] #store processes
num_processes = os.cpu_count() #numper of cpu's on machine best practice

# create processes and asign a function for each process
for i in range(num_processes):
    process = Process(target=square_numbers) #target is callable function executed by this program, if args, args tuple ,args=()
    processes.append(process) #add

# start all processes
for process in processes:
    process.start()

# wait for all processes to finish
# block the main thread until these processes are finished
for process in processes:
    process.join()

print('end main') #only when all processes are done


#Threading
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until child threads are finished
    for thread in threads:
        thread.join()

    #Task manager processes
    #Creates process with 1 main thread and 10 child threads
    #When processessing is finished threads disappear


#More threading
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()


#Threading 2
from threading import Thread
import time

database_value = 0 #simulate db

def increase(): #thread 2 starts from wait time, database value is still 0 at time
    global database_value #in order to modify global variable below
    #database access
    database_value = local_copy #beginning 0

    #processing
    local_copy += 1 #modify copy
    time.sleep(0.1) #intelligently switch to next thread from waiting time
    database_value = local_copy #write new value back into database when done, switches back to thread 1 from sleeping thread 2
        
if __name__ == "__main__":
    print('start value', database_value)
    thread1 = Thread(target=increase) #create thread
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()

    thread1.join() #wait for threads to complete
    thread2.join()

    print('end value', database_value)
    print('end main')

    #value of 1 because of race condition happening when two or more threads try to modify same variable at same time
    #start value 0
    #end value 1
    #end main


#Threading prevent race conditions with locks
from threading import Thread, Lock
import time

database_value = 0 #simulate db

def increase(lock): #give lock given in args 
    global database_value #in order to modify global variable below
    lock.acquire() #has only 2 mthods #lock prevents same time access, locks this state
    #database access
    local_copy = database_value #beginning 0

    #processing
    local_copy += 1 #modify copy
    time.sleep(0.1) #intelligently switch to next thread from waiting time
    database_value = local_copy #write new value back into database when done, switches back to thread 1 from sleeping thread 2
    lock.release() #releases thread1 so thread2 can access and increase
        
if __name__ == "__main__":
    lock = Lock() #create Lock

    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock,)) #comma so python knows its a tuple
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()

    thread1.join() #wait for threads to complete
    thread2.join()

    print('end value', database_value)
    print('end main')

    
# start value 0
# end value 2
# end main


#Threading prevent race conditions instead of acquire, release use with
from threading import Thread, Lock
import time

database_value = 0 #simulate db

def increase(lock): #give lock given in args 
    global database_value #in order to modify global variable below
    with lock:#recommeneded way to use locks as a context manager
        #database access
        local_copy = database_value #beginning 0

        #processing
        local_copy += 1 #modify copy
        time.sleep(0.1) #intelligently switch to next thread from waiting time
        database_value = local_copy #write new value back into database when done, switches back to thread 1 from sleeping thread 2
        
if __name__ == "__main__":
    lock = Lock() #create Lock

    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock,)) #comma so python knows its a tuple
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()

    thread1.join() #wait for threads to complete
    thread2.join()

    print('end value', database_value)
    print('end main')


# start value 0
# end value 2
# end main


#threading queues
#Excellent for thread safe and process safe data exchanges
#Linear data structure that follow the fifo or First in First Out principle
#Example queue of customers waiting in line where customer that came first is also served first
from queue import Queue

# create queue
q = Queue() #create queue object

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1 one is beginning of queue

# now q looks like this:
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1 #queue not only has three and two inside
print(first) 

#check if queue is empty
#q.empty #returns true if queue is empty

#when done processing should call
# q.task_done() #tells program done processing and can continue
# q.join() #blocks until all items in queue have been gotten and processed . 

# q looks like this:
# back --> 3 2 --> front


#threading queues example
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available. gets two arguments queue and lock. get first value in queue

        # do stuff...proccessing
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock)) #target func
        t.daemon = True  # dies when the main thread dies. default isn't daemon thread
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

#     in Thread1 got 0
# in Thread1 got 1
# in Thread1 got 2
# in Thread1 got 3
# in Thread1 got 4
# in Thread1 got 5
# in Thread1 got 6
# in Thread1 got 7
# in Thread1 got 8
# in Thread1 got 9
# in Thread1 got 10
# in Thread1 got 11
# in Thread1 got 12
# in Thread1 got 13
# in Thread1 got 14
# in Thread1 got 15
# in Thread1 got 16
# in Thread1 got 17
# in Thread1 got 18
# in Thread1 got 19
# main done


#threading queues example 2
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q):
    while True:
        value = q.get()  # blocks until the item is available. gets two arguments queue and lock. get first value in queue

        # do stuff...proccessing
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q,)) #target func, tuple comma
        t.daemon = True  # dies when the main thread dies. default isn't daemon thread
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

#what's important is queue can easily exchange data in a thread safe environment
# in Thread2 got 0
# in Thread2 got 1
# in Thread2 got 2
# in Thread2 got 3
# in Thread2 got 4
# in Thread2 got 5
# in Thread2 got 6
# in Thread2 got 7
# in Thread2 got 8
# in Thread2 got 9
# in Thread2 got 10
# in Thread2 got 11
# in Thread2 got 12
# in Thread2 got 13
# in Thread2 got 14
# in Thread2 got 15
# in Thread2 got 16
# in Thread2 got 17
# in Thread2 got 18
# in Thread2 got 19
# main done


#threading queues example 3
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available. gets two arguments queue and lock. get first value in queue

        # do stuff...proccessing
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()
        #no daemon
        #if ....:
            #break

if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock)) #target func, tuple comma
        thread.daemon = True  # dies when the main thread dies. default isn't daemon thread
        thread.start()
    
    # fill the queue with items
    for x in range(1, 21):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done') #when this statement is reached all threads die cause of daemon, while True no longer gets evoked

#what's important is queue can easily exchange data in a thread safe environment

# main done


#multiprocessing
from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choise for the number of processes

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers) #create different processes
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()


#multiprocessing 2
from multiprocessing import Process, Value, Array, #lock #special shared memeory objects array and value
import time

def add_100(number): #lock
    for _ in range(100):
        time.sleep(0.01)
        #lock.acquire()
        number.value += 1
        #lock.release()

def add_100_array(numbers):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1


if __name__ == "__main__":

    #lock = lock()
    shared_number = Value('i', 0) #takes 2 args
    print('Value at beginning:', shared_number.value) #0

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number,)) #lock
    process2 = Process(target=add_100, args=(shared_number,)) #lock

    process3 = Process(target=add_100_array, args=(shared_array,)) #lock
    process4 = Process(target=add_100_array, args=(shared_array,)) #lock

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')

# Value at beginning: 0
# Array at beginning: [0.0, 100.0, 200.0]
# Value at end: 200
# Array at end: [199.0, 300.0, 400.0]
# end main


#multiprocessing 3
from multiprocessing import Process, Value, Array, Lock 
#special shared memeory objects array and value
import time

def add_100(number, lock): 
    for _ in range(100):
        time.sleep(0.01)
        lock.acquire() # or with lock
        number.value += 1
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1


if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0) #takes 2 args
    print('Value at beginning:', shared_number.value) #0

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number, lock)) 
    process2 = Process(target=add_100, args=(shared_number, lock)) 

    process3 = Process(target=add_100_array, args=(shared_array, lock)) #lock
    process4 = Process(target=add_100_array, args=(shared_array, lock)) #lock

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')

# Value at beginning: 0
# Array at beginning: [0.0, 100.0, 200.0]
# Value at end: 200
# Array at end: [199.0, 300.0, 400.0]
# end main


#multiprocessing 4
# import Lock
from multiprocessing import Lock
from multiprocessing import Process, Value, Array
import time

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        # lock the state
        lock.acquire()
        
        number.value += 1
        
        # unlock the state
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            lock.acquire()
            numbers[i] += 1
            lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()
    
    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    # pass the lock to the target function
    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))

    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')


#multiprocessing queues
# import Lock
from multiprocessing import Lock
from multiprocessing import Process, Value, Array
from multiprocessing import Queue #linear data structure
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i) #calculate square and put it in numbers

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q,))

p1.start()
p2.start()

p1.join()
p2.join()

while not q.empty():
    print(q.get()) #return and remove first element in queue

# -1
# -2
# -3
# -4
# -5
# 1
# 4
# 9
# 16
# 25



#multiprocessing pools
from multiprocessing import Pool 
#controls a pool of worker processes to which chops can be submitted
#manage available processes and split
#example data into smaller chunks which can then be processed in parallel by different processes
#takes care of a lot of stuff
#four important methods - map, apply, join, close 

def cube(number): #function is executed and paralleled by difference processes
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool() #create pool

    # by default this allocates the maximum number of available 
    # processors for this task --> os.cpu_count()
    #submits iterable into byte sized chunks and submit to function
    result = p.map(cube,  numbers) #automatically allocate num of processes and create different processes, as many processes as cores on machine
    pool.apply(cube, numbers[1])#have 1 function executed by pool. execute process with 1 argument


    # or 
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close() #wait for pool to process all calculations and return result
    p.join()
    
    print(result)

    # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] #cubed


# Function arguments
# In this article we will talk about function parameters and function arguments in detail. We will learn:

# The difference between arguments and parameters
# Positional and keyword arguments
# Default arguments
# Variable-length arguments (*args and **kwargs)
# Container unpacking into function arguments
# Local vs. global arguments
# Parameter passing (by value or by reference?)
# Arguments and parameters
# Parameters are the variables that are defined or used inside parentheses while defining a function
# Arguments are the value passed for these parameters while calling a function


#arguments and parameters
def print_name(name): # name is the parameter
    print(name)

print_name('Alex') # 'Alex' is the argument


#positional and keyword arguments
def foo(a, b, c):
    print(a, b, c)
    
# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, b=2, c=3)
foo(c=3, b=2, a=1) # Note that the order is not important here

# mix of both
foo(1, b=2, c=3)

# This is not allowed:
# foo(1, b=2, 3) # positional argument after keyword argument
# foo(1, b=2, a=3) # multiple values for argument 'a'

#Default arguments must be at end
def foo(a, b, c, d=4):
    print(a, b, c, d)
foo(1, 2, 3)

#Provide different value for default
foo(1, 2, 3, 7)


#variable length arguments
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
