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