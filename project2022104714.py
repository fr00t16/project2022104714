# write by number int dari 0 - 92
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(92):
	value = randint(0,92)
	print(value)