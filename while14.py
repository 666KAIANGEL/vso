A = int(input())

K = 0
S = 0

while S + 1 / (K + 1) <= A:
    K += 1
    S += 1 / K

print(K,S)