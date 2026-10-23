# TODO: parte 02 taividade 01
''''
Crie um programa que faça as seguintes operações:
-Cadastrar novo usuário (nome, email, telefone, cpf)
-Lista todos os usuários cadastrados 
-Altera os dados de um usuário
-Exclui um usuário 
-Grava os dados de todos os usuários em um .json
-Abre arquivo .json e lista todos os usuários cadastrados nele 
'''
import os 
import json

usuarios = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Cadastrar novo usuário")
    print("2 - Vizualizar usuários cadastrados")
    print("3 - Alterar dados de um usuário")
    print("4 - Excluir usuário")
    print("5 - Gravar arquivo JSON")
    print("6 - Abrir arquivo JSON")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            usuario={}

            usuario ['nome'] = input("Infome o nome: ").strip().title()
            usuario ['cpf'] = input("Informe o cpf: ").strip()
            usuario ['email'] = input("Informe o e-mail: ").strip().lower()

            usuarios.append(usuario)

            print(f"{usuario.get('nome')} CADASTRADO(a) COM SUCESSO!")
            continue
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
                continue
        case "3":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            prosseguir = input("Informe o nome da chave que seja alterar ou f para encerrar: ").strip().lower()

            if prosseguir:
                usuario[prosseguir] = input("Informe o novo valor: ").strip()
                continue
            else:
                break
        case "4":
            # TODO
            pass
        case "5":
            # TODO
            pass
        case "6":
            # TODO
            pass
        case _:
            print("Opção inválida!")
            continue 
        




            
        
        
        

