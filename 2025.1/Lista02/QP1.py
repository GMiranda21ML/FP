while (True):
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    if x > 0 and y > 0:
        print("Primeiro")
    elif x < 0 and y > 0:
        print("Segundo")
    elif x < 0 and y < 0:
        print("Terceiro")
    elif x > 0 and y < 0:
        print("Quarto")
    else:
        break
