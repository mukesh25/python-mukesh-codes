# *
# *       
# *       
# *        				7*5 LED PANEL
# *        
# *         
# * * * * *
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if col == 0:
			print('*',end=' ')
		elif row == 6:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()