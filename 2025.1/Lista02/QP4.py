time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

golsTime1 = int(input("Digite a quantidade de gols que o primeiro time fez: "))
golsTime2 = int(input("Digite a quantidade de gols que o segundo time fez: "))

if golsTime1 > golsTime2:
    print(f"O time {time1} venceu a partida contra o time {time2} de {golsTime1}x{golsTime2}")
elif golsTime1 < golsTime2:
    print(f"O time {time2} venceu a partida contra o time {time1} de {golsTime2}x{golsTime1}")
else:
    print("EMPATE")