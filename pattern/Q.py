#   * * * 
# *       * 
# *       *
# *       *				7*5 LED PANEL
# *  *    * 
# *    *  *  
#   * * *

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row==0 and col in {1,2,3}:
			print('*',end=' ')
		elif row in {1,2,4,5,6} and col in {0,4}:
			print('*',end=' ')
		elif row==3:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()