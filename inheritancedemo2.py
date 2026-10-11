#!/usr/bin/python3
class superclass:
	def properties(self):
		self.age=30
		self.name='Ali Aqdas'
#print(superclass.age)
#print(superclass.name)
obj=superclass()
obj.properties()
print(obj.age)
obj.age=40
print(obj.age)
#print(superclass.age)
