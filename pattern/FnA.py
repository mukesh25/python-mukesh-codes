# * * * * 
# *       * 
# *       *
# * * * * *				7*5 LED PANEL
# *       * 
# *       *  
# * * * *

def print_row(*col):
	for i in range(5): #0 to 4
		if i in col:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()

def B():
	print_row(0,1,2,3)
	print_row(0,4)
	print_row(0,4)
	print_row(0,1,2,3)
	print_row(0,4)
	print_row(0,4)
	print_row(0,1,2,3)
B()