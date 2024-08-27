import random 
empate = 0
ganhou = 0
perdeu = 0

while True:
   
    robo = random.randint(0,2)
    print("VAMOS JOGAR PEDRA PAPEL TESOURA")
    jg = int(input("Escolha e digite corretamente --> 0)pedra,1)papel,2)tesoura // OU 3)sair para terminar o jogo e ver os results"))
    
    if jg == robo:
        empate +=1
        print("empate")
    if jg == 0 and robo == 2:
        ganhou += 1
        print("ganhou")
    if jg == 2 and robo == 1:
        print("ganhou")
        ganhou += 1
    if jg == 1 and robo == 0 :
        print("ganhou")
        ganhou += 1
    #Casos de perder
    if jg == 0 and robo == 1:
        print("perdeu")
        perdeu += 1
    if jg == 1 and robo == 2:
        print("perdeu")
        perdeu += 1
    if jg == 2 and robo == 0:
        print("perdeu")
        perdeu += 1
    if jg == 3:
        print(f"foram {ganhou} vencidas {perdeu} derrotadas e {empate} empates contra o robo")
        break
    