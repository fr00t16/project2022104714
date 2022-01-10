# write by number int dari 0 - 341
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(341):
	value = randint(0,341)
	print(value)