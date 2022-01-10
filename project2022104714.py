# write by number int dari 0 - 525
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(525):
	value = randint(0,525)
	print(value)