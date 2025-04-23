maiorQue8 = 0
soma = 0

menor = 11  
nomeMenor = ""

i = 0
while i < 5:
    nome = input("Digite o nome do posto (ou SAIR para encerrar): ")
    
    if nome == "SAIR":
        break

    indice = float(input("Digite o índice de satisfação (0 a 10): "))

    if indice > 8.0:
        maiorQue8 += 1

    if indice < menor:
        menor = indice
        nomeMenor = nome

    soma += indice

    i += 1

print("\nResultados da análise:")
print("Quantidade de postos com índice de satisfação maior que 8.0:", maiorQue8)
print("Nome do posto com o menor índice de satisfação:", nomeMenor)
print("Soma total dos índices de satisfação:", soma)