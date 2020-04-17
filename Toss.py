from random import randint

I = input('Press Enter to Toss a Coin\
	\n************************\n')

def Toss():
	val = randint(1,2)
	if val == 1:
		return	print('Its a Head\n')

	else:
		return	print('Its a Tail\n')

while bool(I) is False:
	Toss()
	I = input('************************\
		\nPress Enter to Toss Again\nor Anything & Enter to Quit.\n')