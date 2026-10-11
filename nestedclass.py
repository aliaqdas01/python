#!/usr/bin/python3
class outer:
	def __init__(self):
		self.age=38
		self.name='Amit Kumar'
#		self.objj=outer.inner()
	class  inner:
		city='kanpur'
		def __init__(self):
			self.city='lucknow'
#			self.objj=inner()
if __name__=='__main__':
	obj=outer()
	objj=outer.inner()
	print(obj.age)
	print(obj.name)
	print(objj.city)

