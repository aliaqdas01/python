#!/usr/bin/python3
def frequency(s):
	myset=set()
	for i in range(0,len(s)):
		if s[i]==' ':
			continue
		myset.add(s[i])
	print(len(myset))
s='lucknow junction'
frequency(s)

