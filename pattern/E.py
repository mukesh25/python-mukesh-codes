# * * * * *
# *       
# *       
# * * * * *         				7*5 LED PANEL
# *        
# *         
# * * * * *
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row in {0,3,6}:
			print('*',end=' ')
		elif row in {1,2,4,5} and col==0:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()