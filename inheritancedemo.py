#!/usr/bin/python3
class superclass:
	def add(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y
class subclass(superclass):
	def sum(Self,x,y,z):
		return x+y+z
obj=subclass()
print(obj.add(3,4))
print(obj.sub(3,1))
print(obj.sum(3,4,5))

