from src.ejercicio1 import *
from pytest import MonkeyPatch
import pytest

"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
"""


def test_input_numero_normal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'5')
    input_prueba = solicitar_num()
    assert input_prueba == 5

"""
def test_solicitar_numero_pero_se_ingresa_0(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'0')
    input_prueba = solicitar_num()
    assert input_prueba == 0

def test_solicitar_numero_pero_se_ingresa_una_letra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'a')
    with pytest.raises(Exception) as e:
        input_prueba = solicitar_num()
    assert e.type == ValueError
"""
def test_obtener_edades_funcionamiento_normal():
    assert obtener_edades(15) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
def test_sacar_texto():
    assert crear_mensaje_edad(15) == "Esta persona ha cumplido 15 años" 