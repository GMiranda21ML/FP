import os

nomes = []
idades = []

funcionarios = int(input("Digite quantos funcionarios estao aptos a aposentadoria: "))

i = 0
while i < funcionarios:
    nome = input("Digite o nome do funcionario: ")
    idade = int(input("Digite a idade do funcionario: "))

    if idade < 60:
        print("Este funcionario nao pode se aposentar!!")
    else:
        nomes.append(nome)
        idades.append(idade)
        i += 1

maisVelho = idades.index(max(idades))
mediaIdades = sum(idades) / funcionarios


os.system("cls")
print("Funcionários a se aposentar em 2025")
print("***********************************\n")

for i in range(funcionarios):
    print(f"Nome: {nomes[i]}\t\tIdade: {idades[i]} anos")

print(f"\nFuncionário mais antigo: {nomes[maisVelho]}")
print(f"Média de idades das aposentadorias: {mediaIdades:.0f} anos")