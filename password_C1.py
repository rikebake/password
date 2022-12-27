password = 'a123456' #real password
trial = 3 # the # of trial left for users to input the password / maximum trial = 3 
while trial > 0:
	user_input = input('input the password ')
	trial = trial - 1
	if user_input == password:
		print('Welcome!!')
		break
	elif trial > 0:
		print('incorrect,you got ',trial,' times left')
	elif trial == 0:
		print('Oops, no chance. You have tried 3 times')   
		#break