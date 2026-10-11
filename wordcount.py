#!/usr/bin/python3
def wordcount(str):
	str=str.strip()
	if len(str)==0:
		return 0
	count=1
	for i in range(0,len(str)):
		if str[i]==' ' or str[i]=='\1':
			count=count+1
	return count
s=' lucknow is the city of nawabs '
result=wordcount(s)
print(result)
