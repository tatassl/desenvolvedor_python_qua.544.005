# TODO: atividade 01
'''
crie um programa que receba o nome, a massa em kg e a altura em metros do usuario, calcule seu IMC (indice de massa corporal) e  finalize informando o diagnostico do usuario com base no valor do IMC (se estiver magro, gordo no peso ideal...)
'''
# NOTE: ATENÇÃO!!! DIVIRTAM-SE!!
import os
os. system("cls" if os.name == "nt" else "clear")

print("=========Seja BEM-VINDO!=========")

try:
    nome = input("Informe seu NOME: ")
    massa = (input("Informe sua MASSA kg: ").replace (',','.'))
    altura = (input("Informe sua ALTURA em metros: ")).replace (',','.')

    peso = float(massa)
    altura = float(altura)
    imc = peso / (altura **2)

    if imc <18.5:
        print(f"{nome} está ABAIXO do peso ideal!")
    elif imc <=24.9:
        print(f"{nome} está no peso NORMAL")
    else:
        print(f"{nome} está com SOBREPESO")

except Exception as e:
        print(f"Não foi possível calcular o imc. {e}.")

print(f"O IMC de {nome} é igual a {imc}")

continuar = input("Deseja CONTINUAR? 'SIM' para prosseguir. Qualquer outo valor para encerrar: ").strip().lower()

    






