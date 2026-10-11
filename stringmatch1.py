#!/usr/bin/python3

#s1='Lucknow junction'
#s2='Lucknow city'

#set1=set(s1)
#set2=set(s2)

#union=set1 | set2
#intersection=set1 & set2

#print("union:", len(union))
#print("intersection:", len(intersection))
def stringmatch(s1,s2):
	set1=set()
	set2s=set()
	for i in range(0,len(s1)):
		set1.add(s1[i])
	for i in range(0,len(s2)):
		set2.add(s2[i])
	union = set1 & set2
	inter = set1 | set2 
	print(len(union))
	print(len(inter))
s1='lucknow junction'
s2='lucknow city'
result=stringmatch(s1,s2)
print(result)
