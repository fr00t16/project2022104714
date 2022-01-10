# write by number int dari 0 - 289
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(289):
	value = randint(0,289)
	print(value)