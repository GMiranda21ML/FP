qnt = 0
while True:
    codigo = input("Digite o codigo do caixão (ou -1 para sair): ")

    if codigo == "-1":
        break

    qnt += 1

print(f"Quantidade de caixões cadastrados: {qnt}")
