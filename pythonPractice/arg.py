#def person(name, *arg):
#	print(name)
#	print(billy)
#person('navin',28,'mumbai',966464)



def person(name, **kwarg):
	print(name)
	for i,j in billy.items():
		print(i,j)
person('navin',age=28,city='mumbai',mob=966464)