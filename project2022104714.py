# write by number int dari 0 - 196
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(196):
	value = randint(0,196)
	print(value)