# TODO: parte 03 ativdade 01 
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhido por ela.
'''
# NOTE: pesquisar pela aceleração da gravidade em cada planeta.
# NOTE: inclua a Lua na lista de planetas.


import modulo

modulo.limpar()
while True: 
    print(f"{'-'*40}Seja bem-vindo!{'-'*40}")
    nome = input("----Informe seu nome: ").strip()
    massa = float(input("----Informe sua massa em kg: ").replace (',','.'))
    planeta = input("----Informe um planeta:  ").strip().title()
    gravidade = None

    modulo.limpar()

    match planeta:
        case "Mercurio":
            gravidade = 3.72
        case "Venus":
            gravidade = 8.87
        case "Marte":
            gravidade = 3.72
        case "Jupiter":
            gravidade = 24.79
        case "Saturno":
            gravidade = 10.44
        case "Urano":
            gravidade = 8.87
        case "Netuno":
            gravidade = 11.15
        case "Lua":
            gravidade = 1.6
        case _: 
            print("Digite um nome válido!")
            continue 

    peso = massa * gravidade
    print(f"----O peso de {nome} em {planeta} é = {peso}")

if __name__ == "__main__":
    main()

    



