#!/usr/bin/python3
myfile=open('/etc/passwd','r')
for line in myfile.readlines():
	print('-'*20)
	print(line)
mydata=myfile.read()
#wfile=open('mydata.txt','w')
#wfile.write(mydata)
#wfile.flush()
#wfile.close()
print(mydata)
#myfile.close()
