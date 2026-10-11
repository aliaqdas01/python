#!/usr/bin/python3
def reverselist(list):
	flag=0
	i=0
	j=len(list)-1
	while i>j:
		flag=1
		list[i],list[j]=list[j],list[i]
		i=i+1
		j=j-1
	else:
		if flag==0:
			print('condition not met')
L=[2,4,6,8,10,12]
print(L)
reverselist(L)
print(L)
