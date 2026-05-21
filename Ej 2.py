from paquete.Input import *

def calcular_potencia(base:int , potencia:int) -> int:
    if potencia == 0:
        return 1
    
    resultadoanterior = calcular_potencia(base , potencia - 1)
    resultado = base * resultadoanterior

    return resultado

base = get_int("Ingrese la base: ")
potencia = get_int("Ingrese el exponente: ")

resultado = calcular_potencia (base , potencia)

print (base , "^" , potencia , "=" , resultado)

