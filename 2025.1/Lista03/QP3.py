matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        if j == 0:
            matriz[i].append(float(input("Salário médio: R$ ")))
        elif j == 1:
            matriz[i].append(int(input("Tempo mínimo de experiência: ")))
        else:
            matriz[i].append(float(input("Valor da hora de trabalho: R$ ")))

print("Salário\t\tExperiência\tHora (R$)")
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}\t\t", end="")
    print() 

somaSalario = 0
for i in range(3):
    somaSalario += matriz[i][0]

media = somaSalario / 3
print(f"\nMédia salarial das 3 profissões: R$ {media:.2f}")

somaDiagonal = 0  
for i in range(3):
    for j in range(3):
        if i == j:
            somaDiagonal += matriz[i][j]

print(f"Soma dos valores da diagonal principal: {somaDiagonal:.2f}")
