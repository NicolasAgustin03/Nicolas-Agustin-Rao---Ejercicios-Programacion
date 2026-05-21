from paquete.Input import *

def suma_digitos(num:int) -> int:
    if num == 0:
        return 0
    
    resto = num % 10
    resultado = num // 10

    suma = resto + suma_digitos(resultado)

    return suma

num = get_int("Ingrese un numero de dos digitos o mas: ")

sumadigitos = suma_digitos(num)

print ("La suma de los digitos de " , num, " es " , sumadigitos)

    