# write by number int dari 0 - 942
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(942):
	value = randint(0,942)
	print(value)