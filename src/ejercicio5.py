

#Entrada

def ingreso_contrasena():
    contrasena= input("Ingrese la contraseña: ")
    return contrasena

#Procesado
def comprobar_contrasena_ingresada(contrasena_original:str,intento_de_contrasena:str)-> bool:
    if contrasena_original == intento_de_contrasena:
        return True
    else:
        raise NameError("Incorrect Password!!")
#Salida

def mostrar_ingreso_acertado_o_no(resultado_intento:bool) -> str:
    if resultado_intento:
        return "Ingresaste correctamente"
    
if __name__ == "__main__":
    contrasena = ingreso_contrasena()
    intento = ingreso_contrasena()
    
    comprobacion = comprobar_contrasena_ingresada(contrasena,intento)
    
    resultado = mostrar_ingreso_acertado_o_no(comprobacion)
    
    print(resultado)