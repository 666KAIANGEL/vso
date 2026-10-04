import random

def PowerA3(A):
   return A*A*A

A = random.randrange(-10,10)
B = PowerA3(A)
print('A = ', A)
print('B = ', B)


A = random.uniform(-10,10)
B = PowerA3(A)
print('A = ', A)
print('B = ', B)