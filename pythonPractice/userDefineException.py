class TooYoungException(Exception):
	def __init__(self,x):
		self.msg=x

class TooOldException(Exception):
	def __init__(self,x):
		self.msg=x

age=int(input('Enter Age:'))
if age>60:
	raise TooYoungException('Plz wait some time ..u will get best match')
elif age<18:
	raise TooOldException('Your age already crossed marriage age.. No chance of') #getting marriage')
else:
	print('You will get match details soon by email')