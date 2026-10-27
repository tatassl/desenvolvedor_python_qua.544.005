# bilbioteca
import os 

# função
def boas_vindas(nome):
    print(f"{nome}, seja bem-vindo!")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# algoritmo principal
limpar()
nome = input("Infomre o seu nome: ").strip().title()
boas_vindas(nome)
