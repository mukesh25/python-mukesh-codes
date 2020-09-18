#   * * * 
# *       *
# *       
# *          				7*5 LED PANEL
# *        
# *       *  
#   * * *
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row in {0,6} and col in {1,2,3}:
			print('*',end=' ')
		elif row in {1,5} and col in {0,4}:
			print('*',end=' ')
		elif row in {2,3,4} and col==0:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()