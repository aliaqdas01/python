#!/usr/bin/python3
def info(age,name):
	print(name)
	print(age)
d={'name':'Amit','age':30}
#info(age=30,name='sumit')
info(**d)
