import random
import math

def Mean(X,Y,Result):
   Result['AMean'] = (X + Y) / 2
   Result['GMean'] = math.sqrt(X * Y)
   return

R = {'AMean' : None, 'GMean' : None}
#A = random.uniform(-10,10)
A = random.randrange(0,10)
B = random.randrange(0,10)
C = random.randrange(0,10)
D = random.randrange(0,10)

print('A = ', A)
print('B = ', B)
print('C = ', C)
print('D = ', D)

print("(A,B)")
Mean(A,B,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])

print("(A,C)")
Mean(A,C,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])

print("(A,D)")
Mean(A,D,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])