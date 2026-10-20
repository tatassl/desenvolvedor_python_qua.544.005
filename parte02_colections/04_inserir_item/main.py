# bibliotecas
import os 

# lista vazia 
tarefas = []

# limpa o terminal 
os.system("cls" if os.name == "nt" else "clear")

# loop 
while True: 
    # menu
    print("1- Inserir nova tarefa na lista")
    print("2- Finalizar e exibir lista")
    opcao = input("Opção desejada: ").strip() #informa a opção desejada 
    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ") #infoma novo item 
            tarefas.append(nova_tarefa) # insere item na lista 
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            
            # exibe a lista 
            for n, tarefa in enumerate(tarefas,start=1):
                print(f"{n}° tarefa: {tarefa}")
            break #encerra o loop
        case _:
            print("Opção inválida")

    
        
        

