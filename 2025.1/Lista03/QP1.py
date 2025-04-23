import os
os.system("cls")

lista  = []

qntMouses = int(input("Digite a quantidade de mouses: "))

for i in range(qntMouses):
    os.system("cls")
    print(f"Mouse {i + 1}: \n")
    print("Digite 1 para necessita da esfera")
    print("Digite 2 para necessita da limpeza")
    print("Digite 3 para necessita troca do cabo ou conector")
    print("Digite 4 para quebrado ou inutilizado")
    op = int(input("Digite a sua opção: "))

    lista.append(op)


qntDefeito1 = lista.count(1)
qntDefeito2 = lista.count(2)
qntDefeito3 = lista.count(3)
qntDefeito4 = lista.count(4)

percenDefeito1 = qntDefeito1 / qntMouses * 100
percenDefeito2 = qntDefeito2 / qntMouses * 100
percenDefeito3 = qntDefeito3 / qntMouses * 100
percenDefeito4 = qntDefeito4 / qntMouses * 100

os.system("cls")
print(f"Quantidade de de mouses: {qntMouses}\n")
print("Situação\t\t\t Quantidade\t\t\t Percentual")
print(f"1- necessita da esfera\t\t\t {qntDefeito1}\t\t\t\t{percenDefeito1:.0f}%")
print(f"2- necessita da limpeza\t\t\t {qntDefeito2}\t\t\t\t{percenDefeito2:.0f}%")
print(f"3- necessita troca do cabo ou conector\t {qntDefeito3}\t\t\t\t{percenDefeito3:.0f}%")
print(f"4- quebrado ou inutilizado\t\t {qntDefeito4}\t\t\t\t{percenDefeito4:.0f}%")