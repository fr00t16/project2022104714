# write by number int dari 0 - 741
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(741):
	value = randint(0,741)
	print(value)