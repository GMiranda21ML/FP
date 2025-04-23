repteis = []
mamiferos = []
aves = []
outros = []

for i in range(10):
    print("Digite 1 para Réptil")
    print("Digite 2 para Mamifero")
    print("Digite 3 para Ave")
    print("Digite 4 para Outro")
    nome = input("Digite o nome do animal: ")
    op = int(input("Digite a categoria do animal de acordo com as opções: "))

    if op == 1:
        repteis.append(nome)
    elif op == 2:
        mamiferos.append(nome)
    elif op == 3:
        aves.append(nome)
    elif op == 4:
        outros.append(nome)
    else:
        print("Opção invalida, por favor digite novamente!")
    
print(f"Répteis: {repteis} quantidade {len(repteis)}")
print(f"Mamiferos: {mamiferos} quantidade {len(mamiferos)}")
print(f"Aves: {aves} quantidade {len(aves)}")
print(f"Outros: {outros} quantidade {len(outros)}")