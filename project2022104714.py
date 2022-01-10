# write by number int dari 0 - 177
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(177):
	value = randint(0,177)
	print(value)