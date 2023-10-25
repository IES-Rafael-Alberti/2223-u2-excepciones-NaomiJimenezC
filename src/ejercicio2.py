"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas
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

def sacar_lista_numeros(numero_ingresado:int)-> list:
    lista_numerica = []
    for numero in range(1,numero_ingresado+1):
        lista_numerica.append(numero)
    return lista_numerica

def obtener_impares_de_una_lista(lista_de_numeros:list)-> list:
    lista_impares = []
    for posible_impar in lista_de_numeros:
        if posible_impar % 2 != 0:
            lista_impares.append(posible_impar)
    return lista_impares

#Salida

def mostrar_impares(lista_impares:list)-> str:
    cadena_impares = "Estos son los impares: "
    for impar in lista_impares:
        if impar != lista_impares[-1]:
            cadena_impares  +=  str(impar) + ","
        else:
            cadena_impares +=  str(impar) + "."
    return cadena_impares

if __name__ == "__main__":
    
    numero_insertado = solicitar_num()
    numeros_sacados = sacar_lista_numeros(numero_insertado)
    numeros_impares_en_la_lista_sacada= obtener_impares_de_una_lista(numeros_sacados)
    impares_sacados = mostrar_impares(numeros_impares_en_la_lista_sacada)
    
    print(impares_sacados)