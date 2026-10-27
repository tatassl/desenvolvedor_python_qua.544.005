# TODO: parte 02 atividade 01
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
            for n, usuario in enumerate(usuarios):
                print(f"Indice {n}: {usuario}")

            indice = int(input("Informe o índice a ser alterado: "))
            os.system("cls" if os.name == "nt" else "clear")

            if indice >=0:
                print("Informe os novos valores")
                usuario={}
                
                usuario ['nome'] = input("Infome o nome: ").strip().title()
                usuario ['cpf'] = input("Informe o cpf: ").strip()
                usuario ['email'] = input("Informe o e-mail: ").strip().lower()
                usuarios.append(usuario)

                print(f"Dados de {usuario.get('nome')} ATUALIZADOS COM SUCESSO!")
                continue
        case "4":
            for n, usuario in enumerate(usuarios):
                print(f"Indice {n}: {usuario}")
            
            excluir_usuario= int(input("Informe o índice do usuário que deseja excluir: "))
            
            if excluir_usuario >=0:
                del usuarios[excluir_usuario]
                print("Usuário EXCLUIDO com SUCESSO!")
            else:
                print("Índice inválido. ")
        case "5":
            prosseguir = input("Deseja gravar os dados? (s/n)").strip().lower()
            
            if prosseguir == "s":
                os.system("cls" if os.name == "nt" else "clear")
                arquivo = input("Informe o nome do arquivo: ").strip()
                with open(f"atv01/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                print("Arquivo json GRAVADO COM SUCESSO!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                continue
        case "6":
            os.system("cls" if os.name == "nt" else "clear")
            try:
                abrir = input("Informe o nome do arquivo que deseja abrir: ").strip()
                with open(f"atv01/{abrir}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print(f'{'-'*40}')
                continue
            except Exception as e:
                print(f"Não foi possível abrir o arquivo> {e}")
            continue
        case _:
            print("Opção inválida!")
            continue 
        




            
        
        
        

