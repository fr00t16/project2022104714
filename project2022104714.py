# write by number int dari 0 - 580
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(580):
	value = randint(0,580)
	print(value)