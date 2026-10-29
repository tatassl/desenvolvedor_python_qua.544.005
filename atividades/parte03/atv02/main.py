# TODO: parte 03 atividade 02
'''
Crie um programa em que o usuário informe um número inteiro e o programa retorne a sequência Fibonacci.
'''
import os 

print(f"{'-'*40}Seja bem-vindo!{'-'*40}")
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    numero= int(input("Informe um numero inteiro: "))

    a, b = 0,1 
    sequencia = []

    for _ in range(numero):
        sequencia.append(a)
        a, b = b, a + b

    print(f"Sequência Fibonacci: {sequencia}")

if __name__ == "__main__":
    main()
