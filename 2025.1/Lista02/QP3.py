while True:
    ph = int(input("Digite o valor do pH para ser analisado (ou digite -1 para sair): "))

    if ph == -1:
        print("Saindo...")
        break

    if ph < 7:
        print("ACIDA")
    elif ph > 7:
        print("BASICA")
    else:
        print("NEUTRA")
