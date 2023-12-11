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