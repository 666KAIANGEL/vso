A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = 0

for i in range (B - 1,A,-1):
    print(i)
    C += 1
print(C)