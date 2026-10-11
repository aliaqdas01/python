#!/usr/bin/python3
class Myclass:
	age=40
	def add(self,x,y):
		return  x+y
print(list(Myclass.__dict__))
print(Myclass.__dict__['age'])
#print(Myclass['age'])
obj=Myclass()
#obj.add(2,5)
print(list(obj.__dict__))
obj.name='Ali Aqdas'
print(list(obj.__dict__))
print(obj.name)
print(obj.age)
print(obj.__dict__['name'])
print(obj.__dict__['age'])
