#!/usr/bin/python3
class Myclass:
	pass
def printdata(obj):
	print('hello world')
Myclass.mymethod=printdata
Myclass.mymethod('x')
m=Myclass()
m.mymethod()
