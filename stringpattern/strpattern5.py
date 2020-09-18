# write a program to REVERSE internal content of each word?
#  input = Durga software solutions  
#  output =sagrud erawtfos snoitulos
 

s = input('enter some string to reverse: ')
l = s.split()	
print(l)	#['durga','software','solutions']
l1=[]
for word in l:
	l1.append(word[::-1])
print(l1)
output = ' '.join(l1)
print(output)
