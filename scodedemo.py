#!/usr/bin/python3
x=40
def myfn():
	x=10
	print(x)
	def mf():
		x=20
		print(x)
	mf()
	print(x)
myfn()
print(x)
