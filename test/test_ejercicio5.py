from src.ejercicio5 import *
import pytest


def test_comprobar_contrasena_correcta():
    assert comprobar_contrasena_ingresada("patata","patata") == True

def test_comprobar_contrasena_incorrecta():
    with pytest.raises(NameError):
        comprobar_contrasena_ingresada("patata","avellana")