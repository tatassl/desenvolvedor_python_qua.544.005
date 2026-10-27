import os

os.system("csl" if os.name == "nt" else "clear")

nome = input("Informe o seu nome: ").strip().title()
idade = int(input("Informe sua idade: " ))
idade_minima = None

#menu de filmes 
while True:
    print(f"{'-'*20} CINE COBRA {'-'*20}")
    print("Sala 1 - A Roda Qudrada - Livre")
    print("Sala 2 - A Volta dos que não foram - 12 Anos")
    print("Sala 3 - As Tranças do Rei Careca - 14 Anos")
    print("Sala 4 - Poeira em Alto Mar - 16 Anos")
    print("Sala 5 - A vingaça do Peixe Frito - 18 Anos ")

    #usuário informa a sala do filme desejado
    sala = input("Sala desejada: ").strip()

    #atribui a idade minima do filme 
    match sala:
        case "1":
            idade_minima = 0 
        case "2":
            idade_minima = 12
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        case _:
            print("Sala inexistente.")
    
    idade_minima = idade +1
    #verificação de idade 
    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}")
        print("Tenhs um bom filme!")
        break 
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Ingresso negado para {nome}")
        print("Você não possui a idade minima para ver o filme!")
        print("Por favor, escolha outro film: ")
        continue 