matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        if j == 0:
            matriz[i].append(int(input("Digite um valor de Lucia: ")))
        elif j == 1:
            matriz[i].append(int(input("Digite um valor de Bruno: ")))
        else:
            matriz[i].append(int(input("Digite um valor de Rafael: ")))

somaLucia = 0
somaBruno = 0
somaRafael = 0

for i in range(3):
    somaLucia += matriz[i][0]
    somaBruno += matriz[i][1]
    somaRafael += matriz[i][2]

print("Robô de Lúcia\tRobô de Bruno\tRobô Rafael")
for i in range(3):
    for j in range(3):
        print(F"{matriz[i][j]}", end="\t\t")
    print()

if somaLucia == somaBruno == somaLucia:
    print("EMPATE")
elif somaLucia > somaBruno and somaLucia > somaRafael:
    print(f"O robô de Lúcia foi o vencedor com {somaLucia} pontos")
elif somaBruno > somaRafael and somaBruno > somaLucia:
    print(f"O robô de Bruno foi o vencedor com {somaBruno} pontos")
else:
    print(f"O robô de Rafael foi o vencedor com {somaRafael} pontos")