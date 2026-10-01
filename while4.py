N = int(input())

while N % 3 == 0:
    N //= 3

if N == 1:
    print(True)
else:
    print(False)