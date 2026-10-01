N = int(input())
K = int(input())

q = 0
r = N

while r >= K:
    r -= K
    q += 1

print(q,r)
