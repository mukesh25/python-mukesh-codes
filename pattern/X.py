# *       *
#   *   *
#     *
# 	*	*			7*5 LED PANEL
# *       *
# *       *
# *       *  
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row in {0,6}:
			print('*',end=' ')
		elif row in {1,2,3,4,5} and col==2:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()