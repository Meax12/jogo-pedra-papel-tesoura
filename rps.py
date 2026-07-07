from datetime import datetime
import random

while True:
    #data em tempo real
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio" , "junho", "julho", "agosto", "setembro", "novembro", "dezembro"
    ]

    data_hora = datetime.now()
    print(f"{data_hora.day} de {meses[data_hora.month-1]}")

    print(data_hora.strftime("%H:%M:%S"))
    print("")
    #jogo começa:
    print("Vamos jogar pedra papel tesoura! ")
    computador = random.randrange(3)
    jogador = int(input("ESCOLHA: 0 - PEDRA | 1 - PAPEL | 2 - TESOURA | 5 - SAIR "))

    print(f"Você escolheu: {jogador}.")
  
  #SAÍDA
    if jogador == 5:
        print("Obrigado por jogar!. Tchau!")
        break    
       
     
    print(f"Computador jogou: {computador}")
#JOGO  
    if jogador == computador:
        print("EMPATE!")
    elif jogador == 0 and computador == 2:
        print("voce venceu")
    elif jogador == 2 and computador == 1:
        print("voce venceu")
    elif jogador == 1 and computador == 0:
        print("você venceu")
    elif jogador >= 3:
        print(" jogador, escolhe somente de 0 a 2!")
    else:
        print("PERDEU!")
       
        


        
