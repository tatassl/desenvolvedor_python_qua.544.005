# bibliotecas
import os 
import math


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def eq_2o_grau(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta > 0:
        X1 = (-b+math.sqrt(delta))/(2*a)
        X2 = (-b-math.sqrt(delta))/(2*a)
        yield X1
        yield X2
    elif delta == 0:
        X = -b/(2*a)
        yield X 
    else:
        yield "Não existem raizes reais."
        