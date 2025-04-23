qntMaior7 = 0
somaMedias = 0
menorMedia = 0
nomeMenorMedia = ""

i = 1

while i <= 5:
    print(f"\nEscola {i}")
    nome = input("Nome da escola: ")
    media = float(input("Média geral dos alunos: "))

    somaMedias = somaMedias + media

    if media > 7.0:
        qntMaior7 = qntMaior7 + 1

    if i == 1:
        menorMedia = media
        nomeMenorMedia = nome
    elif media < menorMedia:
        menorMedia = media
        nomeMenorMedia = nome

    i = i + 1

print("\nRESULTADOS:")
print("Quantidade de escolas com média superior a 7.0:", qntMaior7)
print("Escola com a menor média:", nomeMenorMedia)