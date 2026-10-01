N = int(input())

K = 0
P = 1

while P * 3 < N:
    P *= 3
    K += 1

print(K)