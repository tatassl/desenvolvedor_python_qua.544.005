# tupla
dias_da_semana =(
    'Domingo',
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado'
)
# exibe a tupla
for dia in dias_da_semana:
    print(dia)
# NOTE se tentar altera a tupla, o programa dá erro. Exemplo:
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possivel ordenar. {e}.0")
finally:
    print("Programa encerrado.")
