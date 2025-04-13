n = int(input("Massivin ölçüsünü daxil et: "))
B = []
for i in range(n):
    element = int(input(f"B[{i}] = "))
    B.append(element)
cem = 0
for i in range(1, n, 2):  
    cem += B[i]
print("Tək indeksli elementlərin cəmi:", cem)
