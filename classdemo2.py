#!/usr/bin/python3
class Myclass:
	def setdata(self,value):
		self.data=value
	def display(self):
		print(self.data)
class Mclass(Myclass):
	def display(self):
		print('kanpur')
m=Mclass()
m.setdata('mumbai')
m.display()
#m.show()
