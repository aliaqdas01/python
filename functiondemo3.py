#!/usr/bin/python3
def myfn():
	print("Hello")
myfn()

def myfn():
	print('Hi')
myfn()

def abc(x):
	print(x)
abc.y='Lucknow'
abc('kanpur')
print(abc.y)

lambda arg1,agr2,arg3: arg1+arg2+arg3
mylmbda = lambda x,y,z: x+y+z
x=mylmbda(2,4,6)
print(x)

def myfn(x):
	print('Lucknow')
	x()
def abc():
	print("kanpur")
myfn(abc)
abc()

myfn(lambda : print('kanpur'))

marks=[30,45,76,35,78]
dmarks=(map(lambda x:x*2,marks))
print(marks)
print(list(dmarks))
evenmarks=filter(lambda x:x%2==0,marks)
print(list(evenmarks))

name='lucknow'
newname=list(map(lambda x:x.upper(),name))
a=' '.join(newname)
print(a)

def mux(x,y):
	return x*y
a=mux(2,5)
print(a)

b=mux('lucknow',2)
print(b)

c=mux(3.14,2)
print(c)
