import random

def PowerA234(A,B):
   B[0] = A * A
   B[1] = B[0] * A
   B[2] = B[1] * A
   return

A = random.randrange(-10,10)
B = [None] * 3
PowerA234(A,B)
print('A = ', A)
print('B = ', B)


A = random.uniform(-10,10)
PowerA234(A,B)
print('A = ', A)
print('B = ', B)