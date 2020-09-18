# *         * 
# * *       * 
# *   *     *
# *     *   *				6*6 LED PANEL
# *       * * 
# *         *  
for row in range(6): #0 to 5
	for col in range(6): # 0 to 5
		if col in {0,5}:
			print('*',end=' ')
		elif row==1 and col==1:
			print('*',end=' ')
		elif row==2 and col==2:
			print('*',end=' ')
		elif row==3 and col==3:
			print('*',end=' ')
		elif row==4 and col==4:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()