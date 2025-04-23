jogadores = [7, 8, 9, 10, 11]
votos = [0, 0, 0, 0, 0]  

print("Enquete: Quem foi o melhor jogador da partida?")
print("Digite o número do jogador (entre 7 e 11). Digite 0 para encerrar a votação.\n")

totalVotos = 0

while True:
    voto = int(input("Número do jogador (0 para encerrar): "))

    if voto == 0:
        break
    elif voto in jogadores:
        indice = jogadores.index(voto)
        votos[indice] += 1
        totalVotos += 1
    else:
        print("Número inválido. Informe um valor entre 7 e 11 ou 0 para sair.")

print("\nResultado da votação:")
print(f"Total de votos válidos: {totalVotos}\n")

print("Jogador\t\tVotos\t\tPercentual")
maiorVoto = 0
melhorJogador = 0

for i in range(len(jogadores)):
    if votos[i] > 0:
        percentual = (votos[i] / totalVotos) * 100
        print(f"{jogadores[i]}\t\t{votos[i]}\t\t{percentual:.2f}%")
        
        if votos[i] > maiorVoto:
            maiorVoto = votos[i]
            melhorJogador = jogadores[i]

if totalVotos > 0:
    percentual_melhor = (maiorVoto / totalVotos) * 100
    print(f"\nO melhor jogador foi o número {melhorJogador}, com {maiorVoto} votos ({percentual_melhor:.2f}%).")
else:
    print("Nenhum voto foi computado.")