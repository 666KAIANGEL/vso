P = int(input())

S = 1000
K = 0

while S <= 1100:
    S += S * P / 100
    K += 1

print(K,S)