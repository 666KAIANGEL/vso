N = int(input())

K = 0
P = 1

while P <= N:
    P *= 3
    K += 1

print(K)