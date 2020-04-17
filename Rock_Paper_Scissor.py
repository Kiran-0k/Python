from random import randint
########################################
val = input('Enter: \t 1 for Rock \n\t 2 for Paper \n\t 3 for Scissor\n\n\t')
comp = randint(0,2)
List  =  ['Rock', 'Paper', 'Scissor']
List1 = ['1', '2', '3']
#########################################
def Lost():
	print('You Lost :-(')
def Won():
	print('You Won!')
def Result():
	print(f'{List[int(conv_val)]} vs {List[comp]}')
######################################### 
if str(val) in List1:
	conv_val = int(val)-1
	if int(conv_val) == comp:
		Result()
		print('It\'s a tie!')

	else:
		Result()
		if int(conv_val) == 0:
			if comp == 1:
				Lost()

			if comp == 2:
				Won()

		elif int(conv_val) == 1:
			if comp == 0:
				Won()

			if comp == 2:
				Lost()

		elif int(conv_val) == 2:
			if comp == 0:
				Lost()

			if comp == 1:
				Won()

else:
	print(f'{val} Is not a correct Option')