# write by number int dari 0 - 619
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(619):
	value = randint(0,619)
	print(value)