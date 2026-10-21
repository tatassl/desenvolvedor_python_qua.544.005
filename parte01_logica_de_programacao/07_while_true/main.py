import os

#limpa a tela 
os. system("cls" if os.name == "nt" else "clear")

# loop 
while True: 
    aluno = input("Infome o nome do aluno: ").strip().title()

    try:
        nota = float(input("Infome a nota de 0 a 10: ").replace (',','.'))

        if nota>= 0 and nota <=10:
            if nota >= 7:
                print(f"{aluno} está APROVADO(A).")
            elif nota >= 5:
                print(f"{aluno} está de RECUPERAÇÃO.")
                
            else:
                print(f"{aluno} está de REPROVADO(A)")
        else:
            print("Nota inválida")
    except Exception as e:
        print(f"Não foi possível calcular a média. {e}.")
    continuar = input("Deseja inserir outra nota? 'sim' para prosseguir. Qualquer outo valor para encerrar: ").strip().lower()

    if continuar == "sim":
        os. system("cls" if os.name == "nt" else "clear")
        continue
    else:
        break
