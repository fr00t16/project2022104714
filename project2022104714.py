# write by number int dari 0 - 519
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(519):
	value = randint(0,519)
	print(value)