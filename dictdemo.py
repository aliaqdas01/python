#!/usr/bin/python3
D={'name':'Ali Aqdas','age': 23,'city':'lucknow'}
print(D['name'])
D['age']=45
print(D['age'])
D['country']='India'
print(D)
info={'firstname':'ali','lastname':'aqdas','age':32}
for key in info:
	print(info[key])

l=list(info.keys())
for x in l:
	print(info[x])
d=dict(a=4,b=3,**dict(c=9,d=7))
print(d)
d2=dict(a=4,b=3,m=dict(c=9,d=7))
print(d2)
d3={'name':'ajay','age':30}
d4={'city':'lucknow',**d2}
print(d4)
