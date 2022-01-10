# write by number int dari 0 - 38
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(38):
	value = randint(0,38)
	print(value)