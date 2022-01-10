# write by number int dari 0 - 567
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(567):
	value = randint(0,567)
	print(value)