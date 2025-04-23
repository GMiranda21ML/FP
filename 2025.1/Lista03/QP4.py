matriz = [[], [], []]

for i in range(3):
    print(f"\nDisciplina {i + 1}:")
    for j in range(3):
        if j == 0:
            matriz[i].append(float(input("Nota da Unidade 1: ")))
        elif j == 1:
            matriz[i].append(float(input("Nota da Unidade 2: ")))
        else:
            matriz[i].append(float(input("Frequência (ex: 0.80): ")))

print("Nota U1\t\tNota U2\t\tFrequência")
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:.2f}\t\t", end="")
    print()

somaU1 = 0
for i in range(3):
    somaU1 += matriz[i][0]

mediaU1 = somaU1 / 3
print(f"\nMédia das notas da Unidade 1: {mediaU1:.2f}")

menorFrequencia = matriz[0][2]
for i in range(1, 3):
    if matriz[i][2] < menorFrequencia:
        menorFrequencia = matriz[i][2]

print(f"Menor frequência: {menorFrequencia:.2f}")
