#!/usr/bin/python3
class Myclass:
	def __init__(self):
		self.age=30
		self.name='Ali Aqdas'
class childclass(Myclass):
	def __init__(self):
		self.city='lucknow'
		super().__init__()
if __name__=='__main__':
	obj=childclass()
	print(obj.city)
	print(obj.age)
	print(obj.name)
