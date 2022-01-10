# write by number int dari 0 - 659
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(659):
	value = randint(0,659)
	print(value)