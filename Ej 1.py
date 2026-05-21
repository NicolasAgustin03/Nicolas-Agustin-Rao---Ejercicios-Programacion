from paquete.Input import *

def sumar_naturales(num:int) -> int:
    if num <= 0:
        return 0
    
    nanterior = sumar_naturales(num - 1)
    suma = num + nanterior

    return suma

numero = get_int("Ingrese un numero (mayor a 0): ")
suma = sumar_naturales(numero)

print ("La suma de los numeros naturales desde 1 hasta" , numero , "es" , suma)
