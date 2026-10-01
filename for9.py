A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = 1

for i in range(A,B + 1):
    C += (i + 1)**2

print(C)