from datetime import datetime
import random

while True:
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio" , "junho", "julho", "agosto", "setembro", "novembro", "dezembro"
    ]

    data_hora = datetime.now()
    print(f"{data_hora.day} de {meses[data_hora.month-1]} de {data_hora}")
    print("Vamos jogar pedra papel tesoura! ")
    computador = random.randrange(3)
    jogador = int(input("ESCOLHA: 0 - PEDRA | 1 - PAPEL | 2 - TESOURA "))

    print(f"Você jogou: {jogador}. Computador jogou: {computador}.")

    if jogador == computador:
        print("EMPATE!")
    elif jogador == 0 and computador == 2:
        print("voce venceu")
    elif jogador == 2 and computador == 1:
        print("voce venceu")
    elif jogador == 1 and computador == 0:
        print("você venceu")
    else:
        print("PERDEU!")
        
       
        


        
