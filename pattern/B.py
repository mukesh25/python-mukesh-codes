# * * * * 
# *       * 
# *       *
# * * * * *				7*5 LED PANEL
# *       * 
# *       *  
# * * * *

#First Approach
for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row in {0,3,6} and col in {0,1,2,3}:
			print('*',end=' ')
		elif row in {1,2,4,5} and col in {0,4}:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
	
#Second Approach
for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if (row % 3 == 0) and (col!=4):
			print('*',end=' ')
		elif (row%3!=0) and (col%4==0):
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()