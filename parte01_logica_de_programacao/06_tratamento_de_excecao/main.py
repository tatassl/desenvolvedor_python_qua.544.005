# tratamento de exceção 
try:
    nome = input("Informe o seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))

    print(f"Nome do usuário: {nome}")
    print(f"Idade do usuário: {idade} anos.")
except Exception as e:
    print(f"NÃO foi possivel executar ação! {e}.")
finally:
    print("Programa finalizado com sucesso!")