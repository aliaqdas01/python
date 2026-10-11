#!/usr/bin/python3
class superclass:
	def __init__(self):
		self.age=30
		self.name='Amit kumar'
	def printer(self):
		print(self.age,self.name)
class subclass(superclass):
	def __init__(self):
		self.age=20
		self.name='mukesh ambani'
obj=subclass()
obj.printer()
