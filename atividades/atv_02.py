import os
os. system("cls" if os.name == "nt" else "clear")

print("{'-' * 20} BEM-VINDO AO CINEFLA! {'-' * 20}")

nome = input("{'-' * 20} Infome o seu NOME completo: ")
idade = input("{'-' * 20} Infome sua IDADE: ")
lista = int(input("{'-' * 20} Se deseja VIZUALIZAR FILMES EM CARTAZ e suas respectivas salas e classificações, digite '1'. Qualquer outo valor para encerrar: ")).strip().lower() 
classificação = idade

while True: 
    print("{'-' * 20} FILMES EM CARTAZ: " \
        "1- 'A sopa de letrinha'." \
        "CLASSIFICAÇÃO: 1+ " \
        "SALA DE CINEMA: 01" \
        "{'-' * 40}" \
        "2- 'HOMEM ARANHA- VOLTA TOTAL'" \
        "CLASSIFICAÇÃO: 16+" \
        "SALA DE CINEMA: 02" \
        "{'-' * 40}" \
        "3- 'VIDA DE SEREIA' " \
        "CLASSIFICAÇÃO: 1+" \
        "SALA DE CINEMA: 03" \
        "{'-' * 40}" \
        "4- 'NÃO PROCURE O NEMO'" \
        "CLASSIFICAÇÃO: 18+" \
        "SALA DE CINEMA: 04" \
        "{'-' * 40}" \
        "5- 'NEM VELOZES E NEM FURIOSOS' " \
        "CLASSIFICAÇÃO: 14+" \
        "SALA DE CINEMA: 05" 
        "{'-' * 40}")
    
    try:
        sala = int(input("Qual é a sala escolhida? "))

        if {sala} == 01 and {classificação} == 1:
            print("Seu filme é 'A sopa de letrinha'.")
        elif {sala} == 02 and {classificação} == 16:
            print("Seu filme é 'HOMEM ARANHA- VOLTA TOTAL'")
        elif {sala} == 03 and {classificação} == 1:
            print(" Seu filme é 'VIDA DE SEREIA'")
        elif {sala} == 04 and {classificação} == 18:
            print(" Seu filme é 'NÃO PROCURE O NEMO'")
        elif {sala} == 05 and {classificação} ==14:
            print("Seu filme é 'NEM VELOZES E NEM FURIOSOS'")
        else:
            print("OPSS.. seus dados não estão de acordo com os requisitos para vizualização do filme!")
    except Exception as e:
        print(f"Não foi possível realizar a ação. {e}.")

print("Seu filme é na sala {sala}! BOM FILME")





    

        
