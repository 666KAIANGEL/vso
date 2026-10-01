N = int(input())

K = 0
S = 0

while S + K + 1 <= N:
    K += 1
    S += K

print(K,S)