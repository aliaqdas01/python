#!/usr/bin/python3
import sys
x=10
y=10
a=[2,4,6,8]
b=[2,4,6,8]
print(a==b)
print(x==y)
print(a is b)
print(x is y)
print(sys.getrefcount(a))
print(sys.getrefcount(x))
