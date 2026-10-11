#!/usr/bin/python3
def frequencyprint(s):
	freq={}
	for i in range(0,len(s)):
		if s[i]==' ':
			continue;
		if s[i] in freq:
			freq[s[i]]=freq[s[i]] + 1
		else:
			freq[s[i]]=1
	print(freq)
s='Lucknow junction'
frequencyprint(s)

