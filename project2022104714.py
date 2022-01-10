# write by number int dari 0 - 150
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(150):
	value = randint(0,150)
	print(value)