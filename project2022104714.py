# write by number int dari 0 - 174
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(174):
	value = randint(0,174)
	print(value)