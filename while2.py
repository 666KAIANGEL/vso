A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = 0
while A >= B:
    A -= B
    C += 1
print(C)