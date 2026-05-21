from paquete.Input import *

def calcular_fibonacci(num:int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    a = calcular_fibonacci(num - 1)
    b = calcular_fibonacci(num - 2)

    resultado = a + b 

    return resultado


fibonacci = get_int("Ingrese un numero positivo para calcular fibonacci: ")
resultado = calcular_fibonacci(fibonacci)

print ("f" , "(" , fibonacci , ")" , "=" , resultado)