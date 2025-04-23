matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite um valor na posição [{i}][{j}]: ")))

soma = 0
maior = 0
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end="")
        soma += matriz[i][j]

        if maior < matriz[i][0]:
            maior = matriz[i][0]

    print()

media = soma / 9

print(f"Media geral dos niveis de poluição: {media}")
print(f"Maior nivel de poluição: {maior}")
