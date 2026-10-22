# biblioteca
import os

# lista de usuarios vazia
usuarios = []

# limpa terminal 
os.system("cls" if os.name == "nt" else "clear")

# loop 
while True:
    # menu 
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir lista de usuários")
    print("3 - Sair do programa")
    opcao = input("Opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    # verifica opção escolhida 
    match opcao:
        case "1": 
            # cria novo dicionario 
            usuario = {}

            # Insere os dados no dicionario 
            usuario['nome'] =  input("Informe o nome:").strip().title()
            usuario['idade'] = int(input("Infome a idade: "))
            usuario['email'] = input("Infome o e-mail: ").strip().lower()
            usuario['CPF'] = input("Infome o CPF: ").strip()

            # adiciona o ususario na lista 
            usuarios.append(usuario)

            # mensagem de sucesso 
            print(f"{usuario.get('nome')} cadastrado com sucesso!")
            continue
        case "2":
            # exibe a lista de usuarios 
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
        case "3":
            break
        case _:  
            print("Opção inválida")

