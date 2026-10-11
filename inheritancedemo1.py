#!/usr/bin/python3
class superclass:
#	pass
	age=30
	name='ali aqdas'
#superclass.age=30
#superclass.name='Ali Aqdas'
print(superclass.age)
print(superclass.name)
obj=superclass()
print(obj.age)
obj.age=40
print(obj.age)
print(superclass.age)
