# * * * * *
#     * 
#     *
# 	  *				7*5 LED PANEL
#     *
# *   *      
#   *   
 

for row in range(7): #0 to 6
	for col in range(5): # 0 to 4
		if row==0:
			print('*',end=' ')
		elif row in {1,2,3,4,5} and col==2:
			print('*',end=' ')
		elif row == 6 and col==1:
			print('*',end=' ')
		elif row == 5 and col==0:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()