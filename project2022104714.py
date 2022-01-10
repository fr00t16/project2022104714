# write by number int dari 0 - 123
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(123):
	value = randint(0,123)
	print(value)