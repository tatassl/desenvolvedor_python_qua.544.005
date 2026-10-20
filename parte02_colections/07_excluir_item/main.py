# lista
frutas = [
    'Maçã',
    'Pera',
    'Maracujá',
    'Morango',
    'Manga',
    'Melancia',
    'Goiaba'
]

while True:
    for n, fruta in enumerate(frutas):
        print(f"Indice {n}: {fruta}")

    # menu
    print("1 - Alterar fruta")
    print("2 - Encerrar programa")
    opcao = input("Opção desejada: ").strip()

    # verifica opção 
    match opcao: 
        case "1":
            indice = int(input("Infome o indice a ser excluido: "))
            del(frutas[indice]) #exclui indice selecionado 
            print("Fruta excluida com sucesso!")
            continue 
        case "2": 
            break
        case _:
            print("Opção inválida.")
            continue

    
