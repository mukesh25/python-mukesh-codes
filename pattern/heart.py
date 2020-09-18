#   * *   * *  
# *     *     *
# *           *
# 	*	    *			6*7 LED PANEL
#     *   *         
#       *
 
for row in range(6): #0 to 5
	for col in range(7): # 0 to 6
		if row ==0 and col in {1,2,4,5}:
			print('*',end=' ')
		elif row ==1 and col in {0,3,6}:
			print('*',end=' ')
		elif row ==2 and col in {0,6}:
			print('*',end=' ')
		elif row ==3 and col in {1,5}:
			print('*',end=' ')
		elif row ==4 and col in {2,4}:
			print('*',end=' ')
		elif row ==5 and col==3:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
	
print('      ==============2nd way=============    ')

for row in range(6): #0 to 5
	for col in range(7): # 0 to 6
		if row in {1,2} and col in {0,6}:
			print('*',end=' ')
		elif row in {0,3} and col in {1,5}:
			print('*',end=' ')
		elif row in {0,4} and col in {2,4}:
			print('*',end=' ')
		elif row in {1,5} and col ==3:
			print('*',end=' ')
		else:
			print(' ',end=' ')
	print()
	