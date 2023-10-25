from src.ejercicio3 import *


def test_sacar_cuenta_atras_desde_x():
    assert crear_cuenta_atras(3) == [0,1,2,3]

def test_sacar_cuenta_atras_desde_0():
    assert crear_cuenta_atras(0) == [0]

def test_invertir_la_cuenta_atras():
    assert invertir_la_cuenta_atras([0,1,2,3]) == [3,2,1,0]

def test_mostrar_cuenta_atras():
    assert mostrar_cuenta_atras([3,2,1,0]) == "La cuentra atrás iniciará a la de 3,2,1,0."