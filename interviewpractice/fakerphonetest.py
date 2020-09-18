from faker import Faker
from random import *
faker = Faker()
  def phonenumbergen():
	d1=randint(6,9)
	num=str(d1)
	for i in range(9): 
		num=num+str(randint(0,9))
	return int(num)
print(phonenumbergen())
print(phonenumbergen())
print(phonenumbergen())
print(phonenumbergen())
