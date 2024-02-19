from src.ejercicio2 import *


def test_sacar_impares_lista():
    assert obtener_impares_de_una_lista([1,2,3,4]) == [1,3]
    
def test_mostrar_cadena_impares():
    assert mostrar_impares([1,3]) == "Estos son los impares: 1,3."