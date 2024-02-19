"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta,
mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

#Entrada

def solicitar_num() -> int:
    numero_solicitado = input("Ingrese un número entero: ")
    return numero_solicitado

#Procesado

def comprobar_si_se_ingreso_un_numero(posible_numero_ingresado:str):
    try:
        numero_convertido = int(posible_numero_ingresado)
        return numero_convertido
    except ValueError as e:
        raise ValueError("La entrada no es correcta")

#Salida
def mostrar_numero(numero_convertido:int):
    return f"Genial, pasaste un número real si llegaste hasta acá {numero_convertido} "

if __name__ == "__main__":
    numero_a_comprobar = solicitar_num()
    comprobar = comprobar_si_se_ingreso_un_numero(numero_a_comprobar)
    numero_pillado = mostrar_numero(comprobar)
    
    print(numero_pillado)