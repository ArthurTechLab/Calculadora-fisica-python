def energia_cinetica():
    objeto = input("Qual é o objeto? ")
    
    while True:
        massa = input(f"Qual a massa do(a) {objeto} em KG? ").lower().strip()

                    
        if "kg" in massa:
            massa = massa.replace("kg", "")
            massa = float(massa)
            break
        
        try:
            massa = float(massa)
            break
        except:
            print("Digite algo valido ou em kg")
            continue
            
       
            
             

    while True:
        velocidade = input(f"Qual a velocidade em m/s do(a) {objeto}? ").lower().strip()

        if "m/s" in velocidade:
            velocidade = velocidade.replace("m/s", "")
            velocidade = float(velocidade)
            break
            
        try:
            velocidade = float(velocidade)
            break
        except:
            print("Digite algo valido ou em m/s")
       

      

        

    cinetica = (massa * velocidade**2) / 2

    print(f"A energia cinética do {objeto} é {cinetica:.2f}J")


def velocidade():
    objeto = input("Qual o objeto? ")
    while True:
        distancia = input("Qual a distancia em metros? ").lower().strip()

        if "m" in distancia:
            distancia = distancia.replace("m", "")
            distancia = float(distancia)
            break
        try:
            distancia = float(distancia)
            break
        except:
            print("Digite algo valido ou em M")



    while True:
        tempo = input(f"Quanto tempo o {objeto} demora para percorrer {distancia}? ").lower().strip()

        if "s" in tempo:
            tempo = tempo.replace("s", "")
            tempo = float(tempo)
            break
        try:
            tempo = float(tempo)
            break
        except:
            print("Digite Algo valido ou em S")
            continue
        

    velocidade = distancia / tempo

    print(f"A velocidade desse(a) {objeto} é {velocidade:.3f}m/s")

def forca():
    objeto = input("Qual o objeto? ")
    while True:
        massa = input(f"Qual a massa do(a) {objeto}? em kg ").lower().strip()

        if "kg" in massa:
            massa = massa.replace("kg", "")
            massa = float(massa)
            break
        
        
        try:
            massa = float(massa)
            break
        except:
            print("Digite Algo valido ou em kg")
            continue

        
    while True:        
        aceleracao = input(f"Qual a aceleração em m/s desse(a) {objeto}? ").lower().strip()


        if "m/s" in aceleracao:
            aceleracao = aceleracao.replace("m/s", "")
            aceleracao = float(aceleracao)
            break

        try:
            aceleracao = float(aceleracao)
            break
        except:
            print("Digite Algo valido ou em m/s")



    forca = massa * aceleracao

    print(f"A força em Newtons desse(a) {objeto} é {forca:.1f}N")


while True:
    print("===CALCULADORA FÍSICA===")
    print("1- Energia Cinética")
    print("2- velocidade")
    print("3- Força")
    print("4- sair")
    
    opcao = int(input("Escolha uma opção "))

    if opcao == 1:
        energia_cinetica()
    
    elif opcao == 2:
        velocidade()
    
    elif opcao == 3:
        forca()
    

    elif opcao == 4:
        break

    else:
        print("opcão invalida!")
