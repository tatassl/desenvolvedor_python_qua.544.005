import os 
from model import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="", cpf="",email="", idade =0 , altura = 0.0)

    limpar()
    usuario.nome = input("informe o nome: ").strip().title()
    usuario.cpf = input("informe CPF: ").strip()
    usuario.email = input("informe o email: ").strip().lower()
    usuario.idade = int(input("informe a idade: "))
    usuario.altura = float(input("informe a altura : ").replace(",","."))

    limpar()
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Idade: {usuario.idade}")
    print(f"Atura: {usuario.nome}")


if __name__ == "__main__":
    main()