#entrada de dados 
nome = input("Infome seu nome: ").strip().title()
massa = float(input("Infome a sua massa em kg: ").replace (',','.'))
altura = float(input('Infome sua altura em metros: ').replace (',','.'))

#calacula o imc 
imc = massa/ (altura **2)

#exibe o valor do imc 
print(f"{nome}, seu IMC é {imc: .2f}!")

#infoma o diagnóstico de usúarios 
if imc < 18.5:
    print("Você está com a massa abaixo do normal.")
elif imc < 25:
    print("Você está com a massa normal.")
elif imc < 30:
    print("Você está com massa acima do normal.")
elif imc < 35:
    print("Você está obeso.")
elif imc < 40:
    print("Você está com obesidade nível II.")
else:
    print("Você está com obesidade mórbida")
