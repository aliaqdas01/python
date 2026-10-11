#!/usr/bin/python3
def outer():
	x=10
	def inner():
		nonlocal x
		#x=20
		print(x)
		x=x+1
	return inner
#x=mydemo()
#x()
fn=outer()
fn()
