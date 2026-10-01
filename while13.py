A = int(input())

K = 0
S = 0

while S <= A:
    K += 1
    S += 1 / K

print(K,S)
