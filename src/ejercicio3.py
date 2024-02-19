"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
Deberá solicitar el número hasta introducir uno correcto. 
"""

#Entrada

def solicitar_num() -> int:
    numero_solicitado = input("Ingrese un número igual o superior a 1: ")
    try:
        while numero_solicitado.isdigit() != True or int(numero_solicitado) < 1:
            numero_solicitado = input("Ingrese un número igual o superior a 1: ")
        return int(numero_solicitado)
    except ValueError as e:
        print("Números como ³ no funcionan")

#Procesado

def crear_cuenta_atras(inicio_cuenta_atras:int)-> list:
    cuenta_atras = []
    for segundo in range(0,inicio_cuenta_atras+1):
        cuenta_atras.append(segundo)
    return cuenta_atras

def invertir_la_cuenta_atras(cuenta_atras_mal_ordenada:list)-> list:
    cuenta_ordenada = sorted(cuenta_atras_mal_ordenada,reverse= True)
    return cuenta_ordenada

#Salida

def mostrar_cuenta_atras(cuenta_atras:list)->str:
    inicio_cuenta_atras = "La cuentra atrás iniciará a la de "
    for segundo in cuenta_atras:
        if segundo != cuenta_atras[-1]:
            inicio_cuenta_atras += str(segundo)+","
        else:
            inicio_cuenta_atras += str(segundo)+"."
    return inicio_cuenta_atras


if __name__ == "__main__":
    segundos_cuenta_atras = solicitar_num()
    generar_cuenta_atras = crear_cuenta_atras(segundos_cuenta_atras)
    ordenar_cuenta_atras = ordenar_cuenta_atras(generar_cuenta_atras)
    
    frase_cuenta_atras = mostrar_cuenta_atras(ordenar_cuenta_atras)
    
    print(frase_cuenta_atras)