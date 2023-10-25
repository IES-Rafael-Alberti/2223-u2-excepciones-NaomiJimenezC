"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
"""


# Entrada

def solicitar_num() -> int:
    numero_solicitado = input("Ingrese un número igual o superior a 1: ")
    try:
        while numero_solicitado.isdigit() != True or int(numero_solicitado) < 1:
            numero_solicitado = input("Ingrese un número igual o superior a 1: ")
        return int(numero_solicitado)
    except ValueError as e:
        print("Números como ³ no funcionan")
#Procesado

def obtener_edades(edad_ingresada:int)-> list:
    edades = []
    for edad in range(1,edad_ingresada+1):
        edades.append(edad)
    return edades
#Salida

def crear_mensaje_edad(edad_cumplida:int)-> str:
    return f"Esta persona ha cumplido {edad_cumplida} años" 
     

if __name__ == "__main__":
    edad_usuario = solicitar_num()
    edades_cumplidas = obtener_edades(edad_usuario)
    
    for edad_cumplida in edades_cumplidas:
        mensaje_edad = crear_mensaje_edad(edad_cumplida)
        print(mensaje_edad)