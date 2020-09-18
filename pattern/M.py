# *       * 
# * *   * * 
# *   *   *
# *       *				7*5 LED PANEL
# *       * 
# *       *  
# *       *
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if col in {0,4}:
			print('*',end=' ')
		elif row==1 and col in {0,1,3,4}:
			print('*',end=' ')
		elif row==2 and col ==2:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()