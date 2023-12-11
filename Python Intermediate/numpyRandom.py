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

np.random.seed(1)
print(np.random.rand(3,3))
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]