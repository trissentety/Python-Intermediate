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