# write by number int dari 0 - 443
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(443):
	value = randint(0,443)
	print(value)