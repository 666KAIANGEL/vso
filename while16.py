P = int(input())

day = 1
run = 10
S = 10

while S <= 200:
    run += run * P / 100
    S += run
    day += 1

print(day,S)