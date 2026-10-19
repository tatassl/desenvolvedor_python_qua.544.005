import os

os.system("cls" if os.name == "nt" else "clear")

print("-" * 20, "BEM-VINDO AO CINEFLA!", "-" * 20)

nome = input("Informe seu nome completo: ").strip()

while True:
    try:
        idade = int(input("Informe sua idade: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
        else:
            break

    except ValueError:
        print("Digite uma idade válida usando números inteiros.")

filmes = {
    1: {
        "nome": "A Sopa de Letrinha",
        "classificacao": 1,
        "sala": 01
    },
    2: {
        "nome": "Homem-Aranha - Volta Total",
        "classificacao": 16,
        "sala": 02
    },
    3: {
        "nome": "Vida de Sereia",
        "classificacao": 1,
        "sala": 03
    },
    4: {
        "nome": "Não Procure o Nemo",
        "classificacao": 18,
        "sala": 04
    },
    5: {
        "nome": "Nem Velozes e Nem Furiosos",
        "classificacao": 14,
        "sala": 05
    }
}

print(f"\nOlá, {nome}! Seja bem-vindo(a) ao CINEFLA!")
print("\n========== FILMES EM CARTAZ ==========")

for numero, filme in filmes.items():
    print(f"\n{numero} - {filme['nome']}")
    print(f"Classificação indicativa: {filme['classificacao']}+")
    print(f"Sala: {filme['sala']}")
    print("-" * 40)

while True:
    try:
        escolha = int(input(
            "\nDigite o número do filme desejado "
            "ou 0 para sair: "
        ))

        if escolha == 0:
            print(f"Até a próxima, {nome}!")
            break

        if escolha not in filmes:
            print("Opção inválida. Escolha um filme de 1 a 5.")
            continue

        filme_escolhido = filmes[escolha]

    
        if idade >= filme_escolhido["classificacao"]:
            print("\nCompra autorizada!")
            print(f"Cliente: {nome}")
            print(f"Filme: {filme_escolhido['nome']}")
            print(f"Sala: {filme_escolhido['sala']}")
            print("Compra concluída com sucesso!")
            print("Bom filme!")

            break

        else:
            print("\nCompra não autorizada!")
            print(
                f"O filme exige idade mínima de "
                f"{filme_escolhido['classificacao']} anos."
            )
            print(
                "Escolha outro filme adequado à sua idade."
            )

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")