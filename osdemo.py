#!/usr/bin/python3
import sys
sys.stdout.write('Hello! world\n')
x=10
y=20
sys.stdout.write(str(x)+','+str(y)+'\n')
temp=sys.stdout
sys.stdout=open('sample.txt','w')
sys.stdout.write('hello,world\n')
sys.stdout.flush()
sys.stdout=temp
