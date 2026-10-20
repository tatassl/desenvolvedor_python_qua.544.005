# bibliotecas
import os

# lista 
nomes = ['Alex', 'Charlotte', 'Scarlet', 'John', 'Jason', 'Michael', 'Connor']   

os.system("cls" if os.name == "nt" else "clear")

# loop
while True: 
    # exibe a lista original
    for n, nome in enumerate (nomes):
        print(f"Indice {n}: {nome}")
    # menu
    print("1- Altera item da lista")  
    print("2- Finaliza")  
    opcao = input("Opção desejada: ").strip() #infoma opção desejada 

    # verifica a opção escolhida
    match opcao:
        case "1":
            # Informa inidce a ser alterado 
            indice = int(input("Infome o indice a ser alterado: ")) 
            # informa novo valor
            nomes[indice] = input("Infome novo nome: ").strip().title()
            os.system("cls" if os.name == "nt" else "clear")
            print("Item da lista alterado com sucesso!")
            continue
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            # exibe nova lista
            for n, nome in enumerate(nomes):
                print(f"Indice {n}: {nome}")
            break
        case _:
            print("Opção inválida")
            continue

